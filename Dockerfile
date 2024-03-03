FROM python:3.11-slim-bullseye AS builder

COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


FROM alpine:3.19.1
COPY --from=builder . .
CMD ["python3", "main.py"]

