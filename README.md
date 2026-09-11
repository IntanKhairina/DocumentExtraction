# Document Intelligence Agent

Extract structured financial data from invoices and receipts.

## Setup

```bash
git clone <your-repo-url>
cd document-intelligence-agent
python3 -m venv venv

# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
python -m api.main
```

Open browser: `http://localhost:8000`

## Usage

1. Click upload button
2. Select PDF or JPG/PNG invoice
3. Click "Upload & Process"
4. View extracted data, validation result, and summary

## Example Response

```json
{
  "document_id": "92f2f7f3",
  "status": "success",
  "structured_data": {
    "vendor": "Green, Sanchez and Shannon",
    "invoice_number": "26388025",
    "invoice_date": "2018-09-01",
    "total_amount": 20.72,
    "currency": "USD"
  },
  "validation": {
    "is_valid": true,
    "errors": [],
    "warnings": []
  },
  "summary": "Invoice from Green, Sanchez and Shannon for USD20.72 due on 2018-10-01."
}
```

## Architecture

- **API**: FastAPI with HTML upload UI
- **Text Extraction**: PyPDF2 + Pytesseract
- **Structured Extraction**: Mock LLM (MVP)
- **Validation**: Pydantic schema validation
- **Orchestration**: Linear agent pipeline

See `ENGINEERING_NOTES.md` for technical details.