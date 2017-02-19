import numpy as np

def descenso_gradiente(X,w,y,dimensiones,cantidad,alfa,epocas,imprimir):
	costos = []

	for epoca in range(0,epocas):
		costos_locales = np.array([])
		for i, xi in enumerate(X):
			xiT = xi.transpose()
			salida = np.dot(xi,w) #Estimamos el valor de la salida
			error = salida - y[i] #Calculamos el error local
			costo = error ** 2 / 2
			costos_locales = np.append(costos_locales,costo)		
			gradiente = np.dot(xiT, error) / cantidad #Calculamos el gradiente
	        w = w - alfa * gradiente #Actualizamos el vector de pesos
	    
		if (imprimir and epoca % 100 == 0):
			print("epoca " + str(epoca) + ":")
			print("costos"),
			print(np.sum(costos_locales)/cantidad)

		costos.append(np.sum(costos_locales)/cantidad)

	return [costos,w]

def calcular(X,w):
	salida = []

	for i,xi in enumerate(X):
		salida_local = 0
		for j,wj in enumerate(w):
			if j == 0:
				salida_local += wj
				continue

			salida_local += xi[j] * wj 

		salida.append(salida_local)
	
	#salida = np.array(salida)
	return salida

def normalizar(matriz):
	return matriz/np.max(matriz)
