import csv
import os.path

def save_data(campos):
	
	employee_list = []
	exitUp = ''
	
	while exitUp != "no":
		employee = {}
		
		for campo in campos:
			employee[campo] = input(f"Ingrese {campo} del empleado: ")
		
		employee_list.append(employee)
		
		exitUp = input("¿Desea seguir agregando registros? si/no: ")
		
	file_name = input("Ingrese un nombre con el que desee guardar al archivo: ")
	file_name_final = (f"{file_name}.csv")
	
	#valida que si el archivo no existe. Crea uno nuevo
	if not (os.path.isfile(file_name_final)):
		
		
		try:
			with open(file_name_final, 'w', newline = '') as file:
				file_guarda = csv.DictWriter(file, fieldnames = campos)
				
				file_guarda.writeheader()
				file_guarda.writerows(employee_list)
				
				print("Se creo el archivo exitosamente")
				return 
				
		except IOError:
			print("Ocurrio un error al crear el archivo")
	
	#valida si el archivo existe
	if(os.path.isfile(file_name_final)):
		
		user_ask = input("¿Desea sobrescribir el archivo o modificarlo?: s/m")
		
		if (user_ask == 's'):
		 
			try:
				with open(file_name_final, 'w+', newline = '') as file:
					file_guarda = csv.DictWriter(file, fieldnames = campos)
				
					file_guarda.writeheader()
					file_guarda.writerows(employee_list)
					
					print("El archivo se sobrescribio correctamente")
					return 
					
			except IOError:
				print("Ocurrio un error al sobrescribir el archivo")
		
		if (user_ask == 'm'):
			
			try:
				with open(archivo, 'a', newline='') as file:
					file_guarda = csv.DictWriter(file, fieldnames=campos)
					
					#si el archivo no existe le graba el encabezado de los campos
					if not archivo_existe:
						file_guarda.writeheader()

					file_guarda.writerows(employee_list)
					
					print("se guardo correctamente la modificación")
					return 
			
			except IOError:
				print("Ocurrio un error al modificar el archivo")

	return file_name_final

def load_data():
	carga = input("Ingrese el nombre del archivo que quiera leer: ")
	archivo = (f"{carga}.csv")
	
	try:
		with open (archivo, 'r', newline = '') as file:
			lectura_csv = csv.DictReader(file)
			campos = lectura_csv.fieldnames
		
			for linea in lectura_csv:
				print(f"{linea}\n")
	
	except IOError:
		print("El archivo no existe")

def consult_data(archivo, presupuestoDado):
	presupuesto = presupuestoDado
	chequeo = input("Ingrese el nombre del archivo para consultar: ")
	empleados = (f"{chequeo}.csv")
	
	try:
		with open (empleados, 'r', newline = '') as file1, open (archivo, 'r', newline = '') as file2:
		
			employee_csv = csv.reader(file1)
			viatic_csv = csv.reader(file2)
			
			#salteo los encabezados
			next(employee_csv)
			next(viatic_csv)
			
			#empiezo a leer
			employee= next(employee_csv, None)
			viatic= next(viatic_csv, None)
			
			#valido que el legajo sea un entero
			legajo_buscado = input("Ingrese el legajo de la persona a consultar: ")
			try:
				legajo_buscado = int(legajo_buscado)
			except ValueError:
				print("Ingrese un número entero para el legajo")
			
			contador = 0				
			while employee:
				if (not viatic or viatic[0] != employee[0]):
					print("\tNo se registran gastos con ese empleado")			
				
				contador = 0
				gastos = 0
				while(viatic and viatic[0] == employee[0]):
					suma = int(viatic[1])
					gastos += suma								
					
				
					viatic= next(viatic_csv, None)			
					legajo = int(employee[0])
					if (legajo == legajo_buscado):
						if(gastos < presupuesto):
							print(f"Legajo {employee[0]}: {employee[2]} {employee[1]}, gastó ${gastos}")
							
					if(gastos == presupuesto):
						print(f"Legajo {employee[0]}: {employee[2]} {employee[1]}, gastó el equivalente al presupuesto")
						
					if(gastos > presupuesto):
						exceso = gastos - presupuesto
						print(f"Legajo {employee[0]}: {employee[2]} {employee[1]}, gastó ${gastos} y se ha pasado del presupuesto por {exceso}")
					
					
						
				
				employee= next(employee_csv, None)	
			
					
				
	except IOError:
		print("hubo un error en la lectura")

def menu():
	PRESUPUESTO = 5000
	CAMPOS = ['Legajo', 'Apellido', 'Nombre']

	while True:
		print("Elija una opcion: \n 1.Cargar empleados \n 2.Leer archivo \n 3.Consultar gastos \n 4.Salir")
		opcion = input("")
		
		if opcion == "4":
			exit()
		if opcion == "1":
			save_data(CAMPOS)
		if opcion == "2":
			load_data()
		if opcion == "3":
			consult_data("viaticos.csv", PRESUPUESTO)
		else:
			print("Por favor elija una opcion valida")
	
menu()
