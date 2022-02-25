from sqlite3 import connect

conn = connect('model/databases/sys_mercado.db')
cursor = conn.cursor()
