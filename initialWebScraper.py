import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
#url = "https://www.imdb.com/chart/top"
url = "https://www.cdc.gov/flu/about/keyfacts.htm"


# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())

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
