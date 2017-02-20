import numpy as np

def obtener_pesos():
	return leer_archivo("archivos/x01.txt")

def obtener_mortalidad():
	return leer_archivo("archivos/x08.txt")

def obtener_experimento():
	return leer_archivo("archivos/training.txt")

def obtener_validacion():
	return leer_archivo("archivos/test.txt")

def leer_archivo(nombre):
	archivo = open(nombre, "r")	
	X = np.array([])
	y = np.array([])

	for linea in archivo: 
		nueva_linea = ' '.join(linea.split())
		arreglo = nueva_linea.split(' ')
		arreglo_flotante = []

		for i,valor in enumerate(arreglo):
			if i == 0:
				continue

			arreglo_flotante.append(float(valor))

		if len(arreglo_flotante) == 0:
			continue

		nuevo_arreglo = arreglo_flotante[:-1]

		xi = np.array([nuevo_arreglo])
		yi = np.array(arreglo_flotante[-1])

		if X.size == 0:
			X = xi
			y = [yi]
			continue

		if xi.size == 0:
			continue

		X = np.concatenate((X,xi))
		y = np.append(y,yi)

	return [X,y]
