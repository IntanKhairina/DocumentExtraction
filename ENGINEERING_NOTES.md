Engineering Notes

## Architecture
- Linear pipeline: Extract → LLM Structure → Validate → Summarize
- File upload via FastAPI
- Mock LLM extraction for MVP (API stability issues)

## Implementation Details

### Text Extraction
- PyPDF2 for PDFs
- Pytesseract fallback for images
- Focus: pipeline integration, not OCR perfection

### Structured Extraction
- Mock response returns hardcoded invoice schema
- **Note**: Production requires Claude/OpenAI API integration
- Pydantic validation on output

### Validation Tool
- `validate_invoice()` checks required fields
- Validates total_amount > 0
- Returns errors and warnings

### Summary Generation
- LLM-based (mock data used in MVP)
- One-sentence human-readable output

## Limitations (MVP)
- Mock LLM extraction (no real AI model processing)
- No hallucination detection
- No RAG/vector database
- No confidence scoring
- Static file storage (no S3)

## Production Improvements
1. **LLM Integration**: Fix Anthropic/OpenAI API client initialization
2. **Async Processing**: Add Celery + Redis for background jobs
3. **Vector DB**: Store past invoices for comparison (Pinecone)
4. **Confidence Scoring**: Add output confidence metrics
5. **Retry Logic**: Exponential backoff for API failures
6. **Structured Logging**: JSON logs with document_id, processing_time, tokens_used
7. **Cloud Storage**: S3 for document storage

## Testing
- Manual upload via web UI
- Sample invoice: sample_invoice1.jpg
- Response includes structured data, validation, summary

## Tech Stack
- FastAPI (API)
- Pydantic (validation)
- PyPDF2 + Pytesseract (text extraction)
- Groq SDK (ready for production LLM)