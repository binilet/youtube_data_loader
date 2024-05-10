#docker run -it --network=pg_pg_admin_bridge -e DATABASE_URL="postgresql://postgres:postgres@172.20.0.3/YoutubeDataAnalytics" youtube_data_loader


# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
#ENV DATABASE_URL="postgresql://postgres:postgres@postgres/YoutubeDataAnalytics"
#best to use : docker run -e DATABASE_URL="postgresql://your_username:your_password@host.docker.internal/your_database_name" -v /path/to/your/local/data:/app/data your_image_name

ENV DATA_FOLDER="/app/data"

# Run script when the container launches
CMD ["python", "loader.py"]
