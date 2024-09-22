import requests
from send_email import send_email

api_key = "9efabf2188d04726a767a4345bacc81e"
url = "https://newsapi.org/v2/top-headlines?sources=" \
    "techcrunch&apiKey=9efabf2188d04726a767a4345bacc81e"

request = requests.get(url)
content = request.json() #turns into a dictionary
message = ""
for article in content["articles"]:
    message += article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"
    
message = message.encode("utf-8")
send_email(message)