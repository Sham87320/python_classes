#  use the requests library to make HTTP requests by calling its functions and methods.
import requests

#use the BeautifulSoup class to create objects that represent the parsed HTML or XML document.
from bs4 import BeautifulSoup

#you are essentially telling Python to load the pandas library into your current working environment.
import pandas as pd

# Send a GET request to the IMDb top movies page
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.get_text())
