import mysql.connector
from mysql.connector import Error

MYDB = None

def connect():
	global MYDB
	try:
		MYDB = mysql.connector.connect(host='localhost',
						database='inversiones',
						user='admin',
						password='INBT2017')
		if MYDB.is_connected():
			print('CONECTADO A LA BASE DE DATOS')
	except Error as e:
		print("ERROR", e)
	finally:
		MYDB.close()

MYCURSOR = MYDB.cursor()
