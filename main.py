# coding=utf-8

from ejercicio1 import ejercicio_1
from ejercicio2 import ejercicio_2
from transform import transform
from ejercicio3 import ejercicio_3

def main():

	opcion = ""
	opcion2 = ""
	print('Resolución de una Regresión Lineal Múltiple.\n\n')
	print('El primer conjunto de datos (x01) corresponde al peso corporal\n')
	print('en función del peso del cerebro (1 rasgo). El segundo conjunto\n')
	print('de datos (x08) corresponde a la Tasa de Mortalidad (3 rasgos).\n')
	print('El tercer conjunto de datos (Ames Data) corresponde a la evaluacion\n')
	print('del modelo construido con respecto a la muestra de Ames\n\n')	
	while opcion == "":
		print('Seleccione el conjuto de datos de su preferencia:\n')
		print('1) x01\n')
		print('2) x02\n')
		print('3) Ames Data\n')
		opcion = input('Opcion: ')
		opcion = str(opcion)
		if opcion == "1":
			ejercicio_1()
		elif opcion == "2":
			while opcion2 == "":
				print('\nSeleccione la representación deseada:\n')
				print('1) Curva de convergencia (alpha = 0.1)\n')
				print('2) Conjunto de curvas de convergencia para los valores\n')
				print('alpha ={0.1, 0.3, 0.5, 0.7, 0.9, 1}.\n')
				opcion2 = input('Opcion: ')
				opcion2 = str(opcion2)
				if opcion2 == "1" or opcion2 == "2":
					ejercicio_2(opcion2)
				else:
					print('Debe introducir \'1\' o \'2\' \n')
					opcion2 = ""
		elif opcion == "3":
			transform("archivos/training.csv", "archivos/training.txt")
			transform("archivos/test.csv", "archivos/test.txt")
			ejercicio_3()
		else:
			print('\nDebe introducir \'1\', \'2\' o \'3\' \n')
			opcion = ""
	

if __name__ == "__main__":
    main()