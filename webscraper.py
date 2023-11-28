from bs4 import BeautifulSoup
import requests

website = 'https://www.magicsur.cl/66-digimon-card-game-chile'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
result = requests.get(website, headers=headers)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='products row products-grid')

print(box.prettify())