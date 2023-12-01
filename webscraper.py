from bs4 import BeautifulSoup
import requests

def getBox(website, search):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    result = requests.get(website, headers=headers)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('div', class_=search)

    return box


def scrap_magic():
    box = getBox('https://www.magicsur.cl/66-digimon-card-game-chile', 'products row products-grid')
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

def scrap_ThirdImpact():
    box = getBox('https://thirdimpact.cl/categoria-producto/juegos-de-cartas/digimon-card-game/', 'products row row-small large-columns-3 medium-columns-3 small-columns-2')
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
    return products_list


def scrap_magicChile():
    box = getBox('https://magic-chile.cl/tcg/digimon', 'row mb-md-5 mb-4 mx-md-n2 mx-n3')
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
        
    return products_list