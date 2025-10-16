# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dsaidns.atlassian.net/rest/api/3/issue"
API_TOKEN = ""

auth = HTTPBasicAuth("dsaidns@gmail.com", API_TOKEN)


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
    "key": "PK"
    },
    "issuetype": {
      "id": "10013"
    },
    "summary": "My first ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))