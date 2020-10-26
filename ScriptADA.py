def TomaDatos():
	NM = 0
	NA = 0
	NMPA = 0
	MinD = 0
	MaxD = 0
	DS = 0
	contador = 0
	file = open('Instancia.txt', 'r')
	for linea in file.readlines():
		if("NumberOfMeetings = " in linea):
			NM = int(linea[18:21])
		if("NumberOfAgents = " in linea):
			NA = int(linea[17:20])
		if("NumberOfMeetingPerAgent = " in linea):
			NMPA = int(linea[26:30])
		if("MinDisTimeBetweenMeetings = " in linea):
			MinD = int(linea[27:30])
		if("MaxDisTimeBetweenMeetings = " in linea):
			MaxD = int(linea[27:30])
		if("DomainSize = " in linea):
			DS = int(linea[13:16])
	file.close()
TomaDatos()
