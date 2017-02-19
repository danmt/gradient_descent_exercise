import numpy as np
import matplotlib.pyplot as plt
import leer_archivos
from operaciones import calcular, descenso_gradiente, normalizar
import matplotlib.patches as mpatches

def preprocesamiento():
	datos = leer_archivos.obtener_mortalidad()
	X_datos = datos[0]
	y_datos = datos[1]

	X = normalizar(X_datos)
	y = normalizar(y_datos)
	w = np.ones(4)

	x_test = []
	for xi in X:
		xi_valor = np.insert(xi,0,1)
		x_test.append(xi_valor)

	X_plot = np.array(x_test)

	return [X_plot,y,w]

def ejercicio_2_1(iteraciones,costos):
	plt.title("Ejercicio 2.a:")
	plt.xlabel('Iteracion')
	plt.ylabel('Costo')
	plt.plot(np.arange(0,iteraciones), costos, 'k')

def ejercicio_2_2(X,y,w):
	plt.title("Ejercicio 2.b:")
	plt.xlabel('Iteracion')
	plt.ylabel('Costo')

	tasas_de_aprendizaje = [0.1,0.3,0.5,0.7,0.9,1]
	iteraciones = 1000

	black_patch = mpatches.Patch(color='black', label='alfa = 0.1')
	green_patch = mpatches.Patch(color='green', label='alfa = 0.3')
	red_patch = mpatches.Patch(color='red', label='alfa = 0.5')
	blue_patch = mpatches.Patch(color='blue', label='alfa = 0.7')
	yellow_patch = mpatches.Patch(color='yellow', label='alfa = 0.9')
	magenta_patch = mpatches.Patch(color='magenta', label='alfa = 1')
	plt.legend(handles=[black_patch,green_patch,red_patch,blue_patch,yellow_patch,magenta_patch])

	obtener_convergencia(X,y,w,tasas_de_aprendizaje[0],iteraciones,'k')
	obtener_convergencia(X,y,w,tasas_de_aprendizaje[1],iteraciones,'g')
	obtener_convergencia(X,y,w,tasas_de_aprendizaje[2],iteraciones,'r')
	obtener_convergencia(X,y,w,tasas_de_aprendizaje[3],iteraciones,'b')
	obtener_convergencia(X,y,w,tasas_de_aprendizaje[4],iteraciones,'y')
	obtener_convergencia(X,y,w,tasas_de_aprendizaje[5],iteraciones,'m')

def obtener_convergencia(X,y,w,tasa_aprendizaje,iteraciones,color):
	imprimir = False
	gradiente = descenso_gradiente(X,w,y,1,y.size,tasa_aprendizaje,iteraciones,imprimir)
	costos = gradiente[0]
	plt.plot(np.arange(0,iteraciones), costos, color)	

def ejercicio_2(opcion):
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

	if opcion == "a":
		ejercicio_2_1(iteraciones,costos)
	else:
		ejercicio_2_2(X,y,w)

	plt.show()