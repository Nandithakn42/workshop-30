# API stands for Application Programming Interface.
# It allows one application to communicate with another.
# pip install request
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)