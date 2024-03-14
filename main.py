from searchGoogle import search_google
from searchGoogle import google_search_medical_term

from publication import get_publication_date
from dataMethods import get_symptoms_list
from dataMethods import get_year
from webshrinker import get_domain_info
from keywords import get_keywords


#main method
if __name__ == "__main__":
    search_term = "flu"
    #list_of_links =  search_google(search_term)

    #print(list_of_links)

    #get_symptoms_list("https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605")

    #get_year("https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605")
    #get_keywords("https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605")


    google_search_medical_term("flu")







