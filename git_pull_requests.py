import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
pull_requests = requests.get(url)
pull_requests_json = pull_requests.json()
for i in range(len(pull_requests_json)):
    print(pull_requests_json[i]["id"])
               