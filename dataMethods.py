import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from htmldate import find_date
from dateutil import parser


#returns list of symptoms as a list of strings
def get_symptoms_list(url):
    print("inside get_symptoms_list")
    #url = "https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605"
    #url = "https://www.mayoclinic.org/diseases-conditions/e-coli/symptoms-causes/syc-20372058"
    #url = "https://www.mayoclinic.org/diseases-conditions/hiv-aids/symptoms-causes/syc-20373524"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    symptoms_list = soup.find('h2', text='Symptoms').find_next('ul').find_all('li')
    
    
    # Extract symptom text
    symptoms = [symptom.get_text(strip=True) for symptom in symptoms_list]
    print(symptoms)
    return symptoms
   



#returns list of symptoms as a list of strings
def get_symptoms_list(url):
    print("inside get_symptoms_list")
    #url = "https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605"
    #url = "https://www.mayoclinic.org/diseases-conditions/e-coli/symptoms-causes/syc-20372058"
    #url = "https://www.mayoclinic.org/diseases-conditions/hiv-aids/symptoms-causes/syc-20373524"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    symptoms_list = soup.find('h2', text='Symptoms').find_next('ul').find_all('li')
    
    
    # Extract symptom text
    symptoms = [symptom.get_text(strip=True) for symptom in symptoms_list]
    print(symptoms)
    return symptoms

def get_year(url):
    print("inside get year")
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("inside get_year()")
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find elements that may contain the publication date
            date_elements = soup.find_all(['time', 'span', 'div'], {'class': ['date', 'timestamp']})
            print(date_elements)
            # Extract the text content from date elements
            date_texts = [date_element.get_text() for date_element in date_elements]

            # Attempt to parse the publication date using dateutil.parser
            for date_text in date_texts:
                try:
                    publication_date = parser.parse(date_text)
                    return publication_date.year
                except ValueError:
                    pass  # Ignore parsing errors and try the next date text

            # If no valid publication date is found
            return None
        else:
            # If the request was not successful
            print(f"Error: Unable to fetch the page. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    """
    print(find_date(url))


