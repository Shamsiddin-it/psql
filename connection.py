import psycopg2
from crud import password1

conn = psycopg2.connect(database = "education_db", 
                        user = "postgres", 
                        host= 'localhost',
                        password = password1,
                        port = 5432)

