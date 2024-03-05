import requests

from send_email import send_email

topic = "apple"
api_key = '5a4ad388035f41b6a21837f2fd315adc'
url = ('https://newsapi.org/v2/top-headlines?country=IN&category=business&apiKey=5a4ad388035f41b6a21837f2fd315adc')

response = requests.get(url)
content = response.json()

body = " "
for article in content["articles"][:20]:
    title = article.get('title', '')
    description = article.get('description', '')
    url = article.get('url', '')

    if title and description:
        body += +title + '\n' + description + '\n' + url + '\n\n'

body = body.encode("utf-8")
send_email(body)
