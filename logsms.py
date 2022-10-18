import sys
import time
import subprocess
import requests
import readline

class System_decores:
	def funtion_banner():
		try:
			subprocess.run(["bash", "decores_scripts/start_banner.sh"])
		except OSError:
			sys.stdout.write("[-] Error al cargar el banner\n")
	def funtion_presentation():
		try:
			sys.stdout.write("Bienvenido a mi herramienta de envios de mensajes\n")
			sys.stdout.write("Creador : @RobotMain \n")
			sys.stdout.write("Visita mi github https://github.com/RobotMain\n")
		except OSError:
			sys.stdout.write("[-] Error al cargar presentacion\n")

class Sender:
	def funtion_send_sms(phone, message):
		try:
			res = requests.post('https://textbelt.com/text', {
				'phone' : f'+{phone}',
				'message' : f'{message}',
				'key' : 'textbelt'
				})
			print(res.json())
		except OSError:
			sys.stdout.write("[-] Posible error de conexion o error de formato \n")
	def funtion_global():
		try:
			phoner = str(input("$Telefono> "))
			user= len(phoner)
			if user > 15:
				sys.stdout.write("Error, numero de telefono no valido!\n")
				sys.exit()
			if phoner=="":
				sys.stout.write("No ha especificado el numero de telefono BREAK!\n")
				sys.exit()
			if phoner==" ":
				sys.stout.write("No ha especificado el numero de telefono BREAK!\n")
				sys.exit()

			if phoner != "" or user < 16:
				message = str(input("$Mensaje> "))
				if message=="":
					sys.stdout.write("Debes especificar tu mensaje BREAK!\n")
					sys.exit()
				else:
					Sender.funtion_send_sms(phoner, message)
		except OSError:
			sys.stdout.write("Error al ingresar los datos")
System_decores.funtion_banner()
System_decores.funtion_presentation()
Sender.funtion_global()