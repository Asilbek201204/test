import psycopg2

con = psycopg2.connect(
    database='education',
    user='postgres',
    host='localhost',
    password=1210,
    port=5432
)
con.autocommit = True
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS products(
               product_name VARCHAR(25) NOT NULL,
               product_image VARCHAR(125) NOT NULL,
               product_price NUMERIC(15,2) NOT NULL,
               qty INT DEFAULT 1
               )
               
               """)