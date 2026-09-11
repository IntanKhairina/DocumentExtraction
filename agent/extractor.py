# import json
# import os
# from groq import Groq

# def extract_structured_data(raw_text: str) -> dict:
#     api_key = os.getenv("GROQ_API_KEY")
#     if not api_key:
#         return {"error": "GROQ_API_KEY not set"}
    
#     client = Groq(api_key=api_key)
    
#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         max_tokens=500,
#         messages=[{
#             "role": "user",
#             "content": f"""Extract JSON from invoice text: 
# {raw_text[:1000]}

# Return ONLY: {{"vendor": "...", "invoice_number": "...", "invoice_date": "...", "due_date": "...", "total_amount": 0.00, "currency": "..."}}"""
#         }]
#     )
    
#     try:
#         return json.loads(response.choices[0].message.content)
#     except:
#         return {"vendor": "N/A", "invoice_number": "N/A", "total_amount": 0, "currency": "USD"}

import json

def extract_structured_data(raw_text: str) -> dict:
    """Mock extraction - returns sample invoice data"""
    return {
        "document_type": "invoice",
        "vendor": "Green, Sanchez and Shannon",
        "invoice_number": "26388025",
        "invoice_date": "2018-09-01",
        "due_date": "2018-10-01",
        "total_amount": 20.72,
        "currency": "USD",
        "line_items": [
            {
                "description": "14 Colors Women Spaghetti Strap Bodycon Mini Dress",
                "quantity": 4.0,
                "amount": 20.72
            }
        ]
    }