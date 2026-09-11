import uuid
import time
import json
import os
from groq import Groq
from vision.extractor import extract_text
from agent.extractor import extract_structured_data
from tools.validate import validate_invoice

class DocumentProcessor:
    def process(self, file_path: str, file_type: str) -> dict:
        doc_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        try:
            print(f"[{doc_id}] Extracting text...")
            raw_text = extract_text(file_path, file_type)
            
            print(f"[{doc_id}] Extracting structured data...")
            structured = extract_structured_data(raw_text)
            
            if "error" in structured:
                return {"document_id": doc_id, "status": "failed", "error": structured["error"]}
            
            print(f"[{doc_id}] Validating...")
            validation = validate_invoice(structured)
            
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
            return {"document_id": doc_id, "status": "failed", "error": str(e)}
    
        return f"Summary: {str(e)}"
    
    def _generate_summary(self, data: dict) -> str:
        """Generate human-readable summary"""
        try:
            vendor = data.get("vendor", "Unknown")
            total = data.get("total_amount", 0)
            currency = data.get("currency", "USD")
            due_date = data.get("due_date", "N/A")
            
            return f"Invoice from {vendor} for {currency}{total} due on {due_date}."
        except Exception as e:
            return f"Summary: {str(e)}"