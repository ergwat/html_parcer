import requests
import pprint
url = "https://jsonplaceholder.typicode.com/posts"
my_dict =  {
    'title': 'foo',
    'body': 'bar',
    'userId': 1}
response = requests.post(url, data=my_dict)

print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)