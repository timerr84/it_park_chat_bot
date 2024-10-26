import sqlite3
conn = sqlite3.connect('example.db') #мы подключили БД example.db
cursor = conn.cursor() #для выполнения запросов и извлечения данных
cursor.execute('select track from music where rating=5') #select name_prod from product
items = cursor.fetchall()
#print(items)
""" cursor.execute('select * from sqlite_master where type="table"')
tabl =cursor.fetchall()
for tab in tabl:
    print(tab[1]) """
conn.close()