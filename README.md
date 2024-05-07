IMDb Top 50 Movies Scraper
This Python-based web scraper extracts detailed information from IMDb’s Top 50 movies list. The scraper is built using Scrapy and is designed to handle concurrent requests efficiently. Additionally, the scraper is packaged in a Docker container for easy deployment.

Libraries Used
Scrapy
    Purpose: Scrapy is a powerful web crawling and web scraping framework used to extract data from websites. It provides a convenient way to define the structure of web pages and extract desired information using XPath or CSS selectors.
    Usage: Used to build the web scraper, define the structure of IMDb pages, and extract movie details.

BeautifulSoup
    Purpose: BeautifulSoup is a Python library for pulling data out of HTML and XML files. It provides easy-to-use methods for navigating and searching HTML content.
    Usage: Used in conjunction with Scrapy to parse HTML content and extract additional information when needed.

Prerequisites
    Docker installed on your machine
    Basic familiarity with Docker commands

Instructions
# 1 move to project directory
cd imdb_scraper

# 2 build docker image
docker build -t scrapy-imdb-image .

# 3 run docker image
docker run scrapy-imdb-image
