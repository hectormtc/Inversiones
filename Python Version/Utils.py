import datetime
import os

dt = datetime.datetime.now()

def clear():
	os.system('CLS')

def input():
	input("Presionar enter...")
	clear()

def fatal(message):
	error_message = "[!!] Error en: "
	error_message += message
	print(error_message)
	input = ("\nPresionar enter...")
	exit()

def date():
	day   = str(dt.day)
	month = str(dt.month)
	year  = str(dt.year)
	return day+"/"+month+"/"+year


def time():
	hour    = str(dt.hour)
	minute  = str(dt.minute)
	sec     = str(dt.second)
	return hour+":"+min+":"+sec
