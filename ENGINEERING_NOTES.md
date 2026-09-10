# Engineering Notes

## Architecture
- **Linear pipeline**: Extract → LLM Structure → Validate → Summarize
- **No async**: MVP scope. Can add background jobs later.
- **File storage**: Temp `/tmp/uploads`. Use S3 for production.

## Prompt Design
- Schema included in prompt for Pydantic validation
- Structured extraction with strict JSON output
- Summary prompt is simple (1-sentence rule)

## Limitations
- No hallucination detection (confidence scoring = future work)
- No RAG/vector DB (can add past invoice comparison later)
- No retry logic (add exponential backoff for production)
- OCR fallback basic (Tesseract is slow, consider AWS Textract)

## Production Improvements
1. Async processing (Celery + Redis)
2. Vector DB (Pinecone) for invoice comparison
3. Confidence scoring on extraction
4. Retry logic + exponential backoff
5. Logging (structured JSON logs)
6. Rate limiting
7. Input validation (file size, page count)