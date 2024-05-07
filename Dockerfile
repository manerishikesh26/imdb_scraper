# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install any dependencies specified in requirements.txt
RUN pip install scrapy
RUN pip install beautifulsoup4

# Copy the current directory contents into the container at /app
COPY . /app/

WORKDIR /app/imdb_scaper

# Run the spider when the container launches
CMD scrapy crawl imdb
