FROM python:3.7

RUN apt-get update && \
    apt-get install --no-install-recommends -y tesseract-ocr=4.0.0-2 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "read.py"]
