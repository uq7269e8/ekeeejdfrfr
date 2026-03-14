FROM python:3.11-slim

WORKDIR /app

COPY generate_hashtags.py .

RUN pip install --no-cache-dir requests

CMD ["python", "generate_hashtags.py"]
