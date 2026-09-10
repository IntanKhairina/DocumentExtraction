from pydantic import BaseModel

class ValidationResult(BaseModel):
    is_valid: bool
    errors: list[str]
    warnings: list[str]

def validate_invoice(data: dict) -> ValidationResult:
    """Validate extracted invoice data"""
    errors = []
    warnings = []
    
    # Required fields
    required = ["vendor", "invoice_number", "invoice_date", "total_amount", "currency"]
    for field in required:
        if field not in data or not data[field]:
            errors.append(f"Missing: {field}")
    
    # Total amount validation
    if data.get("total_amount"):
        try:
            total = float(data["total_amount"])
            if total <= 0:
                errors.append("Total amount must be > 0")
        except:
            errors.append("Invalid total_amount format")
    
    # Date format check (basic)
    if data.get("invoice_date"):
        if len(str(data["invoice_date"])) < 8:
            warnings.append("Date format might be wrong")
    
    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings
    )