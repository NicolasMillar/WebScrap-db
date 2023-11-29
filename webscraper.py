from bs4 import BeautifulSoup
import requests

def getSoup(website):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    result = requests.get(website, headers=headers)
    content = result.text

    return BeautifulSoup(content, 'lxml')


def scrap_magic():
    soup = getSoup('https://www.magicsur.cl/66-digimon-card-game-chile')
    box = soup.find('div', class_='products row products-grid')
    products_list = []

    if box:
        products = box.find_all('div', class_='product-description')
        
        for product in products:
            current_product = product.find('h2', class_='h3 product-title')
            link_product = current_product.find('a')['href']
            name_product = current_product.find('a').text.strip()
            price_product = product.find('span', class_='product-price').text.strip()

            currentProduct = {
                'name' : name_product,
                'link' : link_product,
                'price' : price_product
            }

            products_list.append(currentProduct)

    return products_list
        
