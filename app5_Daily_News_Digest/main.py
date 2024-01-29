import requests
from app10.send_email import send_email

api_key = "9469a44f602c442eab991a0eee1a3c19"
url = (
    "https://newsapi.org/v2/everything?q=tesla&"
    "from=2023-12-19&sortBy=publishedAt&"
    "apiKey=9469a44f602c442eab991a0eee1a3c19&"
    "language=en"
)

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
