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
			NM = int(linea[18:len(linea)])
		elif("NumberOfAgents = " in linea):
			NA = int(linea[17:len(linea)])
		elif("NumberOfMeetingPerAgent = " in linea):
			NMPA = int(linea[26:len(linea)])
		elif("MinDisTimeBetweenMeetings = " in linea):
			MinD = int(linea[27:len(linea)])
		elif("MaxDisTimeBetweenMeetings = " in linea):
			MaxD = int(linea[27:len(linea)])
		elif("DomainSize = " in linea):
			DS = int(linea[13:len(linea)])	
		elif("Agents ("+str(contador)+"):" in linea):
			separador = " "
			separado = linea[12:len(linea)].split(separador)
			listaAux = []
			for i in separado:
				listaAux.append(int(i))
			listaA.append(listaAux)
			contador+=1
	print(listaA)
	#listaA = listaAgentes(NA, NMPA)
	file.close()
TomaDatos()
string1 = "hola mundo"
contador123 =len(string1)
print(contador123)

