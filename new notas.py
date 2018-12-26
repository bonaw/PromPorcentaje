#ingreso de notas
while True:
	con = raw_input("¿Tienes notas con porcentaje que calcular?")
	prom =0
	final = []
	while con=="si" or con=="Si" or con=="sI" or con=="SI":
		n = float(input("Ingrese una nota y presiona enter (ej: seis ocho = 68):  "))
		p = float(input("Ingrese su porcentaje (ej: 35% = 35):   "))
		k = n*(p/100)
		final.append(k)
		con = raw_input("¿Ingresará otra nota?")
	for i in final:
		prom = prom+i
	
	print ("Su promedio es: ",prom)
	
    
