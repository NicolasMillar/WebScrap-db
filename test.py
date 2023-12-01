from bs4 import BeautifulSoup
import requests

website = 'https://magic-chile.cl/tcg/digimon'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
result = requests.get(website, headers=headers)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='row mb-md-5 mb-4 mx-md-n2 mx-n3')
products_list = []

if box:
    products = box.find_all('div', class_='product-block text-center mb-md-3 mb-2 p-md-3 p-2 rounded trsn')

    for product in products:
        current_product = product.find('div', class_='brand-name small trsn')
        link_product = 'https://magic-chile.cl'
        link_product += current_product.find('a')['href']
        name_product = current_product.find('a').text.strip()
        price_product = product.find('span', class_='product-block-list').text.strip()

        currentProduct = {
            'name' : name_product,
            'link' : link_product,
            'price' : price_product
        }
        
        products_list.append(currentProduct)
    
print(products_list)