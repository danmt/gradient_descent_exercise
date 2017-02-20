import numpy as np
import matplotlib.pyplot as plt
import leer_archivos
from operaciones import calcular, descenso_gradiente, normalizar


def preprocesamiento():
	datos = leer_archivos.obtener_pesos()
	X_datos = datos[0]
	y_datos = datos[1]

	X = normalizar(X_datos)
	y = normalizar(y_datos)
	w = np.ones(2)

	x_test = []
	for xi in X:
		xi_valor = np.insert(xi,0,1)
		x_test.append(xi_valor)

	X_plot = np.array(x_test)

	return [X_plot,y,w]

def ejercicio_1_1(iteraciones,costos):
	convergencia = plt.subplot(211)
	convergencia.set_title("Ejercicio 1.a:")
	convergencia.set_xlabel('Iteracion')
	convergencia.set_ylabel('Costo')
	convergencia.plot(np.arange(0,iteraciones), costos, 'k')

def ejercicio_1_2(x,y,w):
	datos = plt.subplot(212)
	datos.set_title("Ejercicio 1.b:")	
	datos.set_xlabel('Datos')
	datos.set_ylabel('Costo')
	y_prediccion = calcular(x,w)
	datos.plot(x[:,1], y, 'bo', x[:,1], y_prediccion, 'k')

def ejercicio_1():
	datos = preprocesamiento()

	X = datos[0]
	y = datos[1]
	w = datos[2]
	
	iteraciones = 100
	tasa_aprendizaje = 0.1
	imprimir = False

	gradiente = descenso_gradiente(X,w,y,1,y.size,tasa_aprendizaje,iteraciones,imprimir)
	costos = gradiente[0]
	w = gradiente[1]

	grafica = plt.figure(1)
	grafica.suptitle('Ejercicio 1', fontsize=14, fontweight='bold')
	grafica.subplots_adjust(hspace=.5)

	ejercicio_1_1(iteraciones,costos)
	ejercicio_1_2(X,y,w)

	plt.show()