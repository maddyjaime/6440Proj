import requests
import json
from base64 import urlsafe_b64encode

def get_domain_info():
    print("inside get_domain_info()")
    target_website = "https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605"

    key = "Sx1kUG9cmpZ8KaB3oCvX"
    key = "ecgDt4sZniA1uigIFHNV"


    secret_key = "YNLjca2z6NTzr7WWUdlo"
    secret_key = "cTT5ZxdgvTWBugekM3sK"

   # Encode the target_website to bytes
    target_website_bytes = target_website.encode('utf-8')

    # Use urlsafe_b64encode with the bytes-like object
    api_url = "https://api.webshrinker.com/hosts/v3/%s" % urlsafe_b64encode(target_website_bytes).decode('utf-8')

    response = requests.get(api_url, auth=(key, secret_key))
    status_code = response.status_code


    try:
        # Try to parse the response as JSON
        data = response.json()
    except json.decoder.JSONDecodeError:
        # Handle the case where the response is not valid JSON
        data = None

    if status_code == 200 and data:
        # Do something with the JSON response
        print(json.dumps(data, indent=4))
    elif status_code == 400:
        # Bad or malformed HTTP request
        print("Bad or malformed HTTP request")
        print(response.text)
    elif status_code == 401:
        # Unauthorized
        print("Unauthorized - check your access and secret key permissions")
        print(response.text)
    elif status_code == 402:
        # Request limit reached
        print("Account request limit reached")
        print(response.text)
    else:
        # General error occurred
        print(f"A general error occurred (Status Code: {status_code}), try the request again")
        print(response.text)
