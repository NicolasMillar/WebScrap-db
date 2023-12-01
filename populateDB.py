import psycopg2
from webscraper import scrap_magic, scrap_ThirdImpact, scrap_magicChile

dbname = 'wgezdikj'
user = 'wgezdikj'
password = 'Pp96GdIcpkrJNk2Dxp7B5eQmhrNkgTCH'
host = 'bubble.db.elephantsql.com'
port = '5432'

try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    print("Conexión exitosa!")


except Exception as e:
    print(f"Error de conexión: {e}")

finally:
    if connection:
        connection.close()
        print("Conexión cerrada.")

#scraped_productsMagicSur = scrap_magic()
#scraped_productsThirdImpact = scrap_ThirdImpact()
#scraped_productsmagicChile = scrap_magicChile()