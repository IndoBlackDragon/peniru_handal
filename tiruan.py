# encoding : "utf-8"
# author : member tim IndoBlackDragon
# ini hanya kode tiruan


from time import sleep
from os import system
from sys import *

def logo():
	global perusak
	perusak = """____                           _
|  _ \ ___ _ __ _   _ ___  __ _| | __
| |_) / _ \ '__| | | / __|/ _` | |/ /
|  __/  __/ |  | |_| \__ \ (_| |   <
|_|   \___|_|   \__,_|___/\__,_|_|\_\ By IndoBlackdragon👌
		"""

def colors():

		# warna depan	 
	global red,cyan,yellow
	red,cyan,yellow = '\x1b[31;1m','\x1b[36;1m','\x1b[33;1m'

		# warna proses 	 
	global green,blue
	green,blue = "\x1b[32;1m","\x1b[34;1m"

class main:

	def __init__(self,number_phone):

		self.number = number_phone
		self.num = 0

	def proses(self):

		system("clear")

		while True:

			colors()
			txt1 = f'{green}{self.num}{yellow} virus berbahaya telah Dikirim ke {blue}{self.number}'
			txt2 = f'{red}Merusak hp korban....'
			txt3 = f'{blue}Subscribe Ahmad Adptr'
			sleep(0.2)
			print (txt1)
			sleep(0.1)
			print (txt2)
			sleep(0.1)
			print (txt3)
			self.num += 1

def depan():
	system("clear")
	colors()
	logo()

	print ("");print (perusak);print ("")
	print (f'{yellow}tools ini digunakan untuk merusak hp korban')
	sleep(2)

	print (f"{red}Subscribe chanel pembuat script ini")
	print (f"{cyan} IndoBlack ")
	print ("github = https://github.com/IndoBlackDragon/peniru_handal")
	print ("youtube = -")
	sleep(4)
	print ("Whatsapp = 6285342600951")
	sleep(1)

	try:
		Num = int(input(f'{yellow}Nomor hp korban : '))
		sleep(3)
	except ValueError:
		system("clear")
		print (f'tolong masukkan nomor telepon')
		exit()

	print ("")

	program = main(Num)
	program.proses()


if __name__=="__main__":
	depan()
