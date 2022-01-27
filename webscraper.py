from bs4 import BeautifulSoup
import requests

url = 'https://ethans_fake_twitter_site.surge.sh/'
response = request.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print (content)
