# base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy semua file project 
COPY . .

# Install Flask 
RUN pip install flask

# Expose port Flask
EXPOSE 5050

# Jalankan aplikasi
CMD ["python", "app.py"]