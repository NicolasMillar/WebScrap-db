from bs4 import BeautifulSoup
import requests

website = 'https://thirdimpact.cl/categoria-producto/juegos-de-cartas/digimon-card-game/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
result = requests.get(website, headers=headers)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='products row row-small large-columns-3 medium-columns-3 small-columns-2')
common_class = 'product-small'
productos_set = set()

if box:
    products = box.find_all(class_=lambda x: x and common_class in x.split())
    
    for product in products:
            current_product = product.find('p', class_='name product-title woocommerce-loop-product__title')
            link_product = current_product.find('a')['href']
            name_product = current_product.find('a').text.strip()
            price_product = product.find('span', class_='woocommerce-Price-amount amount').text.strip()

            currentProduct = {
                'name' : name_product,
                'link' : link_product,
                'price' : price_product
            }

            productos_set.add(tuple(currentProduct.items()))
            
products_list = [dict(item) for item in productos_set]

print(products_list)