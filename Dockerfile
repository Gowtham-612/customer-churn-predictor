# Stage 1: Build environment
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies only if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies into a temporary directory
RUN pip install --upgrade pip
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Runtime environment
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy project files
COPY . /app

# Set PYTHONPATH to make imports work
ENV PYTHONPATH=/app

# Expose ports for FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Start both apps
CMD ["bash", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port 8501"]
