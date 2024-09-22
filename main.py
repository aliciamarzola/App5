import requests

api_key = "9efabf2188d04726a767a4345bacc81e"
url = "https://newsapi.org/v2/top-headlines?sources=" \
    "techcrunch&apiKey=9efabf2188d04726a767a4345bacc81e"

request = requests.get(url)
content = request.json() #turn into a dict
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])