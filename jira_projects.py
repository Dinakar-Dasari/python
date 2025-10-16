import requests
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from requests.auth import HTTPBasicAuth
import json

url = "https://dsaidns.atlassian.net//rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("dsaidns@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"  # to get the response in JSON format. Without this, the server might send HTML or XML
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = response.json()
print(output[1]["name"])



