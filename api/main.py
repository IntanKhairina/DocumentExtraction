import sys
sys.path.insert(0, '..')

from dotenv import load_dotenv
import os
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
import os
import shutil
from agent.pipeline import DocumentProcessor

app = FastAPI(title="Document Intelligence Agent")
processor = DocumentProcessor()

os.makedirs("/tmp/uploads", exist_ok=True)

@app.get("/")
def home():
    """Serve HTML with upload form"""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Document Intelligence Agent</title>
        <style>
            body { font-family: Arial; margin: 50px; }
            .container { max-width: 600px; }
            input[type="file"] { margin: 10px 0; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
            .result { margin-top: 20px; background: #f0f0f0; padding: 15px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📄 Document Intelligence Agent</h1>
            <p>Upload an invoice (PDF or JPG/PNG)</p>
            
            <form id="uploadForm" enctype="multipart/form-data">
                <input type="file" id="file" name="file" accept=".pdf,.jpg,.jpeg,.png" required>
                <button type="submit">Upload & Process</button>
            </form>
            
            <div id="result" class="result" style="display:none;">
                <pre id="output"></pre>
            </div>
        </div>
        
        <script>
            document.getElementById('uploadForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const formData = new FormData();
                formData.append('file', document.getElementById('file').files[0]);
                
                const response = await fetch('/documents', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                document.getElementById('output').textContent = JSON.stringify(data, null, 2);
                document.getElementById('result').style.display = 'block';
            });
        </script>
    </body>
    </html>
    """)

@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process document"""
    allowed_types = ["application/pdf", "image/jpeg", "image/png"]
    if file.content_type not in allowed_types:
        return JSONResponse(status_code=400, content={"error": "Only PDF, JPG, PNG allowed"})
    
    file_path = f"/tmp/uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    file_type = "pdf" if file.content_type == "application/pdf" else "image"
    result = processor.process(file_path, file_type)
    
    os.remove(file_path)
    return result

@app.get("/health")
def health():
    """Health check"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)