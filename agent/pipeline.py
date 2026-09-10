import uuid
import time
from datetime import datetime
from vision.extractor import extract_text
from agent.extractor import extract_structured_data
from tools.validate import validate_invoice

class DocumentProcessor:
    def process(self, file_path: str, file_type: str) -> dict:
        """Main agent pipeline"""
        doc_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        try:
            # Step 1: Extract text
            print(f"[{doc_id}] Extracting text...")
            raw_text = extract_text(file_path, file_type)
            
            # Step 2: LLM extraction
            print(f"[{doc_id}] Extracting structured data...")
            structured = extract_structured_data(raw_text)
            
            # Step 3: Validation
            print(f"[{doc_id}] Validating...")
            validation = validate_invoice(structured)
            
            # Step 4: Summary
            print(f"[{doc_id}] Generating summary...")
            summary = self._generate_summary(structured)
            
            processing_time = time.time() - start_time
            
            return {
                "document_id": doc_id,
                "status": "success",
                "structured_data": structured,
                "validation": validation.model_dump(),
                "summary": summary,
                "processing_time_seconds": round(processing_time, 2)
            }
        
        except Exception as e:
            return {
                "document_id": doc_id,
                "status": "failed",
                "error": str(e)
            }
    
    def _generate_summary(self, data: dict) -> str:
        """Generate human-readable summary"""
        from anthropic import Anthropic
        
        client = Anthropic()
        response = client.messages.create(
            model="claude-opus-4-1",
            max_tokens=100,
            messages=[{
                "role": "user",
                "content": f"Summarize this invoice in 1 sentence: {data}"
            }]
        )
        return response.content[0].text