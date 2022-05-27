import requests

headers = {"Content-Type": "application/json"}
request = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
print(request.json())