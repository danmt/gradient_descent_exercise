from ejercicio1 import ejercicio_1
from ejercicio2 import ejercicio_2

def main():

	opcion = ""
	opcion2 = ""
	print('Resolución de una Regresión Lineal Múltiple.\n\n')
	print('El primer conjunto de datos (x01) corresponde al peso corporal\n')
	print('en función del peso del cerebro (1 rasgo), mientras que el\n')
	print('el segundo conjunto de datos (x08) corresponde a la Tasa de\n')
	print('Mortalidad (3 rasgos).\n\n')
	while opcion == "":
		print('Seleccione el conjuto de datos de su preferencia:\n')
		print('1) x01\n')
		print('2) x02\n')
		opcion = input('')
		if opcion == "1":
			ejercicio_1()
		elif opcion == "2":
			while opcion2 == "":
				print('Seleccione la representación deseada:\n')
				print('a) Curva de convergencia (alpha = 0.1)\n')
				print('b) Conjunto de curvas de convergencia para los valores\n')
				print('alpha ={0.1, 0.3, 0.5, 0.7, 0.9, 1}.\n')
				opcion2 = input('')
				if opcion2 == "a" or opcion2 == "b":
					ejercicio_2(opcion2)
				else:
					print('Debe introducir \'a\' o \'b\' \n')
					opcion2 = ""
		else:
			print('\nDebe introducir \'1\' o \'2\' \n')
			opcion = ""
	

if __name__ == "__main__":
    main()