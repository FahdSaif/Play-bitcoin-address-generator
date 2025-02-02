# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install ecdsa base58

# Copy the script into the container
COPY generate_address.py /app/generate_address.py

# Run the script when the container starts
CMD ["python", "/app/generate_address.py"]
