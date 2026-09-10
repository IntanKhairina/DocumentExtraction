from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil
from agent.pipeline import DocumentProcessor

app = FastAPI(title="Document Intelligence Agent")
processor = DocumentProcessor()

# Create upload directory
os.makedirs("/tmp/uploads", exist_ok=True)

@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a financial document"""
    
    # Validate file type
    allowed_types = ["application/pdf", "image/jpeg", "image/png"]
    if file.content_type not in allowed_types:
        return JSONResponse(
            status_code=400,
            content={"error": "Only PDF, JPG, PNG allowed"}
        )
    
    # Save file
    file_path = f"/tmp/uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Determine file type
    file_type = "pdf" if file.content_type == "application/pdf" else "image"
    
    # Process
    result = processor.process(file_path, file_type)
    
    # Cleanup
    os.remove(file_path)
    
    return result

@app.get("/health")
def health():
    """Health check"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)