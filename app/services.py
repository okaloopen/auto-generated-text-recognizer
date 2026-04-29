import logging
from typing import Any

import cv2
import numpy as np
import pytesseract
from fastapi import UploadFile

logger = logging.getLogger(__name__)

class OCRService:
    """Service class for performing OCR on uploaded images."""

    def __init__(self) -> None:
        # Initialize any configuration here if needed
        pass

    async def extract_text(self, file: UploadFile) -> str:
        """Read an uploaded image file and extract text using Tesseract.

        Args:
            file: Uploaded image file from the client.

        Returns:
            The recognized text from the image.
        """
        # Read file bytes asynchronously
        contents: bytes = await file.read()
        # Convert bytes data to a NumPy array
        nparr = np.frombuffer(contents, np.uint8)
        # Decode image using OpenCV
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            logger.error("Failed to decode image from uploaded data.")
            raise ValueError("Invalid image data")
        # Convert to grayscale for better OCR results
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Use pytesseract to extract text
        text: str = pytesseract.image_to_string(gray)
        logger.info("Extracted %d characters from uploaded image", len(text))
        return text
