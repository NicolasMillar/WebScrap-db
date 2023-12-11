import os 
from dotenv import load_dotenv
import psycopg2 
from webscraper import scrap_magic, scrap_ThirdImpact, scrap_magicChile
import Levenshtein

def calculate_similarity(product_name, products):
    max_similarity = 0.0
    most_similar_product_id = None

    for product_id, db_product_name in products:
        similarity = Levenshtein.ratio(product_name.lower(), db_product_name.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_product_id = product_id

    return max_similarity, most_similar_product_id


load_dotenv()


try:
    connection = psycopg2.connect(
        dbname=os.getenv('db_name'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        host=os.getenv('db_host'),
        port=os.getenv('db_port', 5432)
    )

    cursor = connection.cursor()
    cursor.execute("SELECT id, productName FROM product")
    products = cursor.fetchall()

    scraped_productsMagicSur = scrap_magic()

    for product in scraped_productsMagicSur:
        threshold = 0.7
        max_similarity, most_similar_id = calculate_similarity(product['name'], products)

        if max_similarity >= threshold:
            cursor.execute("INSERT INTO productData (idProduct, idStore, productPrice) VALUES (%s, %s, %s)", (most_similar_id, 0, product['price']))
            connection.commit()
        print(f"El producto '{product['name']}' tiene una similitud del {max_similarity * 100}% con el producto ID {most_similar_id}")

   
    """
    scraped_productsThirdImpact = scrap_ThirdImpact()
    scraped_productsmagicChile = scrap_magicChile()
    """


except Exception as e:
    print(f"Error de conexión: {e}")

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()
        print("Conexión cerrada.")

