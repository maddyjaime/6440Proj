import requests
from bs4 import BeautifulSoup

def is_informational_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')


            promotional_phrases = ['advertisement', 'ad', 'sponsored', 'promo', 'promotion', 'offer']
            title = soup.title.string.lower() if soup.title else ""
            for phrase in promotional_phrases:
                if phrase in title:
                    return False
            
    
            promotional_classes = ['ad', 'advertisement', 'promo', 'promotion', 'offer']
            for tag in soup.find_all():
                for cls in tag.get('class', []):
                    if cls.lower() in promotional_classes:
                        return False
                for attr in tag.attrs.values():
                    if any(phrase in str(attr).lower() for phrase in promotional_phrases):
                        return False
            
            # If no clear promotional phrases found, consider it as informational
            return True
        else:
            print("Failed to fetch webpage. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None