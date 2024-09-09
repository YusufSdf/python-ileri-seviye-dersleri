import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")
response = requests.get("https://jsonplaceholder.typicode.com/todos",params={
    "userId": "1",
    "completed": "true"
}) # dinamik olduğunda bu


result = response.json()

print(result)