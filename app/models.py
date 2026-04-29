from pydantic import BaseModel

class OCRResponse(BaseModel):
    """Response model for OCR results."""
    text: str
