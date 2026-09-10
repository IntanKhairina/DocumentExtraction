<<<<<<< HEAD
# Document Intelligence Agent

Extract structured financial data from invoices.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY=your_key

# Run server
python api/main.py
```

## Usage

```bash
curl -X POST http://localhost:8000/documents \
  -F "file=@invoice.pdf"
```

## Response

```json
{
  "document_id": "abc123",
  "status": "success",
  "structured_data": {...},
  "validation": {...},
  "summary": "Invoice from ABC Supplies for RM3250 due Feb 15.",
  "processing_time_seconds": 4.2
}
```
=======
# document-intelligence-agent
>>>>>>> 7fde49652ce28dc44a1503cc2e6288d8d9a36b0a
