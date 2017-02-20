import numpy as np
import leer_archivos
from operaciones import calcular, descenso_gradiente, normalizar

def ejercicio_3():
	datos = leer_archivos.obtener_experimento()

	X = datos[0]
	y = datos[1]

	x_test = []
	for xi in X:
		xi_valor = np.insert(xi,0,1)
		x_test.append(xi_valor)

	X_plot = np.array(x_test)

	w = np.ones(X_plot[0].size)

	iteraciones = 1000
	tasa_aprendizaje = 0.1
	imprimir = False
	gradiente = descenso_gradiente(X_plot,w,y,1,y.size,tasa_aprendizaje,iteraciones,imprimir)

	print "Vector de pesos w:"
	print gradiente[1]
	print ""

	validacion = leer_archivos.obtener_validacion()
	vX = validacion[0]
	vy = validacion[1]

	vx_test = []
	for vxi in vX:
		vxi_valor = np.insert(vxi,0,1)
		vx_test.append(vxi_valor)

	vX_plot = np.array(vx_test)

	bias = 0
	acc = 0
	mx = 0
	mad = 0
	mse = 0
	for target in y:
		delta = np.dot(X_plot[acc],gradiente[1]) - target
		bias += delta
		mad += abs(delta)
		mse += delta ** 2 
		if delta > mx:
			mx = delta
		acc+=1
	bias = bias/acc
	mad = mad/acc
	mse = mse/acc

	vbias = 0
	acc = 0
	vmx = 0
	vmad = 0
	vmse = 0
	tt = 0
	for target in vy:
		delta = np.dot(vX_plot[acc],gradiente[1]) - target
		vbias += delta
		vmad+= abs(delta)
		vmse += delta ** 2
		if delta > vmx:
			vmx = delta
		tt+=target
		acc+=1
	vbias = vbias/acc
	vmad = vmad/acc
	vmse = vmse/acc
	tt=tt/acc
	print tt

	print ""
	print "Bias de entrenamiento: " + str(bias)
	print "Desviacion Maxima de entrenamiento: " + str(mx)
	print "Desviacion Absoluta de la Media de entrenamiento: " + str(mad)
	print "Error Cuadratico Medio de entrenamiento: " + str(mse)
	print ""
	print "Bias de prueba: " + str(vbias)
	print "Desviacion Maxima de prueba: " + str(vmx)
	print "Desviacion Absoluta de la media de prueba: " + str(vmad)
	print "Error Cuadratico Medio de prueba: " + str(vmse)
