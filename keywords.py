from summa import keywords
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



def get_keywords(url):
    print("inside get_keywords()")
    response = requests.get(url)

    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    

    #print("title: " + str(soup.title) + "\n")

    """get just text of page"""
    overall_text = soup.get_text()
    #print(type(overall_text))


    # Example text
    text = "Your page text goes here."

    # Extract keywords using TextRank
    kw = keywords.keywords(overall_text)
    print("keywords:")
    print(kw)