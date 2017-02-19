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
	promedio = np.mean(matriz, axis=0)
	desviacion = np.std(matriz, axis=0)
	vector = False
	# en caso de que la matriz sea un vector (una dimensión)
	if(matriz.ndim < 2 ):
		vector = True
		matriz = matriz.reshape(matriz.shape[0],1)
		promedio = np.asarray(promedio).reshape(1,-1)[0,:]
		desviacion = promedio = np.asarray(desviacion).reshape(1,-1)[0,:]
	n,m = matriz.shape
	for i in range (m):
		matriz[:,i] = (matriz[:, i] - promedio[i])/desviacion[i]

	if vector:
		matriz = matriz.reshape(matriz.shape[0],)
		
	return matriz
