import requests
import json

request = requests.get("https://jsonplaceholder.typicode.com/posts")
result = request
result = request.status_code
result = request.headers
result = request.url
result = request.encoding
result = request.text

posts = json.loads(request.text)


print(posts)