# Use a minimal, secure base image (Python slim-buster is relatively small)
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install Flask
RUN pip install flask

# Create app directory
WORKDIR /app

# Copy application files
COPY app.py /app/app.py

# Expose the application port (must match the port used in app.py)
EXPOSE 8080

# Run the application using the non-root user that comes with the slim image
# Note: For production and true STIG compliance, you should explicitly define a non-root user (e.g., USER 1000)
CMD ["python", "app.py"]
