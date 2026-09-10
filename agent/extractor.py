from anthropic import Anthropic
from pydantic import BaseModel
import json

class InvoiceData(BaseModel):
    document_type: str
    vendor: str
    invoice_number: str
    invoice_date: str
    due_date: str = None
    total_amount: float
    currency: str
    line_items: list = None

def extract_structured_data(raw_text: str) -> dict:
    """Use Claude to extract structured invoice data"""
    client = Anthropic()
    
    prompt = f"""Extract invoice information from this text. Return ONLY valid JSON matching this schema:
{{
    "document_type": "invoice",
    "vendor": "...",
    "invoice_number": "...",
    "invoice_date": "YYYY-MM-DD",
    "due_date": "YYYY-MM-DD",
    "total_amount": 0.00,
    "currency": "MYR",
    "line_items": []
}}

TEXT:
{raw_text}

Return ONLY the JSON object, no markdown."""

    response = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    try:
        # Extract JSON from response
        json_str = response.content[0].text
        data = json.loads(json_str)
        return InvoiceData(**data).model_dump()
    except Exception as e:
        return {"error": str(e), "raw_response": response.content[0].text}