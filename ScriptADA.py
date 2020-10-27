import sys
NM = 0
NA = 0
NMPA = 0
MinD = 0
MaxD = 0
DS = 0
MeetingsDistances = list()
AgentsMeetings = list()
def checkArgs(*args):
	if len(sys.argv) < 2:
		print("ERROR: Instancia no especificada")

def crearArray(dato):
	listaAux = []
	for i in dato:
		listaAux.append(int(i))
	return listaAux
def encuentraCamino(NM,listaCoste):
	meetingsPath = 0
	for i in (NM-1):
		meetingsPath = meetingsPath+listaCoste[i][i+1]+1
	return meetingsPath	
def paralelo(i, j, listaAgentes, NA):
	noAtiendenAmbos = True
	for a in NA:
		if(listaAgentes[a][i] == 1 and listaAgentes[a][j] == 1):
			return False
	return noAtiendenAmbos
def Resolucion(NM, NA, NMPA, MinD, MaxD,DS, listaAgentes, listaCoste):
	limiteMax = encuentraCamino(NM, listaCoste)

def getNumbers(Instancia): #Función dedicada a obtener los datos del MSP
	try:
		#Inicar Lector------------------------------------------------------------------#
		file = open(Instancia, 'r')
		content = file.read()
		contentList = content.split('\n\n')
		#Obtener Parametros-------------------------------------------------------------#
		PrettyNumbers = [int(i) for i in contentList[0].split() if i.isdigit()]
		#Obtener y establecer las reuniones de los agentes------------------------------#
		for agent in contentList[1].split('\n'):
			n = [int(i) for i in agent.split() if i.isdigit()]
			if n:
				AgentsMeetings.append(n)
		#Obtener y establecer las distancias entre las reuniones------------------------#
		for meetings in contentList[2].split('\n'):
			n = [int(i) for i in meetings.split() if i.isdigit()]
			if n:
				MeetingsDistances.append(n)
		MeetingsDistances.pop(0)
		file.close()
		#Establecer Parametros----------------------------------------------------------#
		NM 		= PrettyNumbers[0]
		NA		= PrettyNumbers[1]
		NMPA	= PrettyNumbers[2]
		MinD 	= PrettyNumbers[3]
		MaxD 	= PrettyNumbers[4]
		DS		= PrettyNumbers[5]
		#-------------------------------------------------------------------------------#
	except:
		print("ERROR: Instancia no encontrada")

checkArgs()
getNumbers(sys.argv[1])
