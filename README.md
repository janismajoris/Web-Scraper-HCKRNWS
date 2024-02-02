# Hacker News Scraper

## Description

This project is a simple Python script designed to scrape news articles from [Hacker News](https://news.ycombinator.com/). It extracts the titles, links, and scores of the current top articles on the Hacker News homepage. This script is intended for educational purposes, showcasing basic web scraping techniques using Python.

## Purpose

The purpose of this project is to demonstrate how to perform web scraping using Python. It serves as a practical example for those interested in data collection from the web, parsing HTML content, and extracting useful information from websites.

## Technologies Used

- **Python**: The core programming language used for the script.
- **requests**: A Python library used to send HTTP requests to the website.
- **Beautiful Soup 4 (bs4)**: A Python library for parsing HTML and XML documents. It's used here to navigate and search through the HTML structure of the Hacker News page to extract the needed information.

## How It Works

The script performs the following steps:
1. Sends an HTTP GET request to the Hacker News homepage using the `requests` library.
2. Parses the HTML content of the page using Beautiful Soup to find article titles, links, and scores.
3. Extracts and prints the number of articles found, their links, and scores to the console.
4. Organizes the extracted data into a dictionary for easy access and manipulation.

## Usage

To use this script, you will need Python installed on your system along with the `requests` and `BeautifulSoup4` libraries. You can install the required libraries using pip:

## Note

This script is for educational purposes only. Always ensure you have permission to scrape a website and abide by its terms of service.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
