import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
#url = "https://www.imdb.com/chart/top"
url = "https://www.cdc.gov/flu/about/keyfacts.htm"
url = "https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

#print("title: " + str(soup.title) + "\n")

"""get just text of page"""
#print(soup.get_text())

#print(soup.body.get_text())

"""find all of a tag"""
tables = soup.find_all('table') #returns list of only ONE table
#table = tables[0]
#headers = [header.text.strip() for header in tables[0].find_all('th')]
headers = tables[0].find_all('thead')[0].find_all('th') #returns list of headers
tableBody = tables[0].find_all('tr')[2:] #returns list of each row of table

print("headers:")
print(headers)



"""
data_cells = soup.find_all('td', class_='p-1')
result = [cell.find('span').get_text() for cell in data_cells]


print(result)

"""

overall_body_data = []
#iterate over each row
for i in tableBody:
    #result = [cell.find('span').get_text() for cell in data_cells]
    sub_data = []
    #print("_____________________________________")
    #print(i)
    for cell in i:
        #print("inside cell")
        if (cell.get_text() != "\n"):
            print(cell.get_text())
            sub_data.append(cell.get_text() )
    print("_________\n\n\n")
   
    overall_body_data.append(sub_data)


#turn nested list into pandas df
headers_for_table = ["Season", "Predominant Virus(es)", "Season Severity", "0-4 yrs", "5-17 yrs", "18-49 yrs", "50-64 yrs","≥65 yrs"]
df = pd.DataFrame(overall_body_data, columns=headers_for_table)


print("\n\n\n\noverall_body_data: ")
print(overall_body_data)

print("\n\n\n\npands df: ")
print(df)

#cdc
#<meta property="article:published_time" content="2023-05-02">
#<meta property="og:author" content="CDC">
#<meta property="article:author" content="CDC">

#mayo
#<meta name="PublishDate" content="2024-01-10">

#cnn
#<meta property="article:published_time" content="2024-03-05T11:19:01.183Z">

#stat
#<meta property="article:published_time" content="2024-03-05T11:19:01.183Z">

#medinePlus
#<meta name="DC.Date.Modified" content="2024-02-28">




def extract_publication_date(url):
    
    #url = "https://www.cdc.gov/flu/about/keyfacts.htm"
    print("inside extract_publication_date(url): \n\n\n")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print("2 inside extract publication date()")
    
    date_element = soup.find('span', class_='publication-date')

    if date_element:
        print("here is date_element: ")
        print(date_element)
        #date_str = date_element.text.strip()
        # You might need to use a date parsing library like dateutil.parser to parse the date string
        # This example uses dateutil.parser for simplicity
        #return parse(date_str).strftime('%Y-%m-%d')

    print("end of extract_publication_date(url):")
    return None


publication_date = extract_publication_date(soup)
print("publication date: " + str(publication_date))

