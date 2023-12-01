import os
from dotenv import load_dotenv
import psycopg2
from webscraper import scrap_magic, scrap_ThirdImpact, scrap_magicChile

load_dotenv()

try:
    connection = psycopg2.connect(
        dbname=os.getenv('db_name'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password'),
        host=os.getenv('db_host'),
        port=os.getenv('db_port', 5432)
    )

    scraped_productsMagicSur = scrap_magic()
    scraped_productsThirdImpact = scrap_ThirdImpact()
    scraped_productsmagicChile = scrap_magicChile()


except Exception as e:
    print(f"Error de conexión: {e}")

finally:
    if connection:
        connection.close()
        print("Conexión cerrada.")

