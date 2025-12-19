FROM python:3.11-slim

WORKDIR /app

# Copy dependency list first for better caching
COPY requirements.txt .

# Install all Python dependencies (including Jupyter)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
