# Auto-Generated Text Recognizer

## Overview

This project provides an asynchronous API for text recognition using **FastAPI**, **OpenCV**, and **Tesseract**. It allows clients to upload images and receive the extracted text in response. The service is designed with a modular architecture for maintainability and scalability.

## Features

- Upload an image and extract printed text via OCR.
- Asynchronous request handling using FastAPI and Python's `asyncio`.
- Uses OpenCV for reading images and Pytesseract for optical character recognition.
- Structured into separate modules for services, models, and the main application.
- Includes basic logging for visibility into requests and operations.

## Architecture Overview

```
app/
├── __init__.py
├── main.py        # FastAPI application with endpoints
├── services.py    # OCRService encapsulating image loading and text extraction
├── models.py      # Pydantic models for response schemas
requirements.txt   # Project dependencies
README.md          # Project documentation
```

- **main.py** sets up the FastAPI app, defines routes for health checks and OCR, and injects the OCR service.
- **services.py** defines an `OCRService` class with asynchronous methods to load image files using OpenCV and extract text with Pytesseract.
- **models.py** defines response models such as `OCRResponse` for returning extracted text.

## Installation

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) on your system.

2. Clone this repository and create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the application locally:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Usage

- **Health check**

  ```bash
  curl http://127.0.0.1:8000/health
  # {"status": "ok"}
  ```

- **Perform OCR**

  ```bash
  curl -F "file=@path/to/image.jpg" http://127.0.0.1:8000/ocr
  # {"text": "Recognized text here"}
  ```

## API Documentation

| Method | Endpoint | Description |
|-------|----------|-------------|
| GET    | `/health` | Returns a simple status message. |
| POST   | `/ocr`    | Accepts an image file (`file` field) and returns the recognized text. |

FastAPI automatically provides interactive documentation at `/docs` and an OpenAPI schema at `/openapi.json`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes or new features. Make sure to run linters and tests before submitting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
