from googlesearch import search
import requests
from bs4 import BeautifulSoup



def search_google(search_term ):
    return_link_list = []
    """
    print("inside search_google() method\n\n")
    
    for j in search(search_term, tld="co.in", num=10, stop=10, pause=2):
        return_link_list.append(j)
    return return_link_list
    """
    # Run the loop until we have exactly 10 unique links
    while len(return_link_list) < 10:
        try:
            # Perform the Google search
            for link in search(search_term, tld="co.in", num=10, stop=10, pause=2):
                # Check if the link is not already in the list
                if link not in return_link_list:
                    return_link_list.append(link)

                # Break the loop if we have reached 10 unique links
                if len(return_link_list) == 10:
                    break

        except Exception as e:
            print(f"An error occurred: {e}")

    return return_link_list



def google_search_medical_term(medical_term):
    print("inside google_search_medical_term")
    search_query = f"{medical_term} symptoms site:wikipedia.org"
    
    # Perform a Google search and get the top links
    search_results = search(search_query, num=1, stop=1, pause=2)

    # Compile a list to store symptoms
    symptoms_list = []

    # Iterate through the top links
    for result_url in search_results:
        try:
            # Fetch the HTML content of the page
            response = requests.get(result_url)
            if response.status_code == 200:
                print("after 200 code")
                soup = BeautifulSoup(response.text, 'html.parser')
                #print(soup.prettify())
                
                symptoms_section = soup.find('a', {'href': '/wiki/Signs_and_symptoms'})
                print(symptoms_section)
                # Check if the section exists
                if symptoms_section:
                    # Find the parent <td> tag that contains the symptoms
                    td_parent = symptoms_section.find_parent('td')

                    # Extract individual symptoms from the parent
                    symptoms_list = [symptom.text.strip() for symptom in td_parent.find_all('a')]

                    print(symptoms_list)
                else:
                    print("Symptoms section not found.")
        except Exception as e:
            print(f"Error processing URL {result_url}: {e}")

    return symptoms_list
