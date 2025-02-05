# backend/Dockerfile

# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose port for Flask app (default is 5000)
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]


# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# # Run the application
# CMD ["flask", "run", "--host=0.0.0.0"]