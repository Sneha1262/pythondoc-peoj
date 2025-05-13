# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the script
CMD ["python", "app.py"]
