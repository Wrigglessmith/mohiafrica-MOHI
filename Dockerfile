# Use a stable Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Ensure required dependencies are installed
RUN pip install Flask Scrapy gunicorn

# Render dynamically assigns a port
ENV PORT=10000
EXPOSE 10000

# Start the Flask app with gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]

