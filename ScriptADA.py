def TomaDatos():
	NM = 0
	NA = 0
	NMPA = 0
	MinD = 0
	MaxD = 0
	DS = 0
	contador = 0
	listaA = []
	file = open('Instancia.txt', 'r')
	for linea in file.readlines():
		if("NumberOfMeetings = " in linea):
			NM = int(linea[18:21])
		elif("NumberOfAgents = " in linea):
			NA = int(linea[17:20])
		elif("NumberOfMeetingPerAgent = " in linea):
			NMPA = int(linea[26:30])
		elif("MinDisTimeBetweenMeetings = " in linea):
			MinD = int(linea[27:30])
		elif("MaxDisTimeBetweenMeetings = " in linea):
			MaxD = int(linea[27:30])
		elif("DomainSize = " in linea):
			DS = int(linea[13:16])	
		elif("Agents ("+str(contador)+"):" in linea):
			separador = " "
			separado = linea[12:60].split(separador)
			listaAux = []
			for i in separado:
				listaAux.append(int(i))
			listaA.append(listaAux)
			contador+=1
	print(listaA)
	#listaA = listaAgentes(NA, NMPA)
	file.close()
TomaDatos()
