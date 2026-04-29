import logging
from fastapi import FastAPI, UploadFile, File, HTTPException

from .services import OCRService
from .models import OCRResponse

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Auto-Generated Text Recognizer")

# Initialize the OCR service
ocr_service = OCRService()

@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/ocr", response_model=OCRResponse)
async def perform_ocr(file: UploadFile = File(...)) -> OCRResponse:
    """Endpoint to perform OCR on an uploaded image.

    Args:
        file: The uploaded image file.

    Returns:
        An OCRResponse containing the extracted text.

    Raises:
        HTTPException: If OCR fails or invalid image is provided.
    """
    try:
        text = await ocr_service.extract_text(file)
        return OCRResponse(text=text)
    except Exception as exc:
        logger.error("Error performing OCR: %s", exc)
        raise HTTPException(status_code=400, detail=str(exc))
