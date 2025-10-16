import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
pull_requests = requests.get(url)
print(pull_requests)
print("\n")
pull_requests_json = pull_requests.json()
print(pull_requests_json)
# for i in range(len(pull_requests_json)):
#     print(pull_requests_json[i]["id"])
               