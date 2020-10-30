import sys
NM = 0
NA = 0
NMPA = 0
MinD = 0
MaxD = 0
DS = 0
MeetingsDistances = {}
AgentsMeetings = {}
result=list()
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
	for i in range(0,NM-1):
		meetingsPath = meetingsPath+listaCoste[i][i+1]+1
	return meetingsPath	
def paralelo(i, j, listaAgentes, NA):
	noAtiendenAmbos = True
	for a in range(0,NA):
		if(listaAgentes[a][i] == 1 and listaAgentes[a][j] == 1):
			return False
	return noAtiendenAmbos
def encontrarAgentes(meeting):
	retorno=list()
	for i in range(0,len(AgentsMeetings)):
		if(meeting in AgentsMeetings[i]):
			retorno.append(i)
	return retorno
#def Resolucion():
#	for i in AgentsMeetings:
#		for j in i.values():
			

#	for i in range(0,len(AgentsMeetings)):
#		for n in range(0,len(AgentsMeetings[1].getValues())):
#			meeting=AgentsMeetings[i][n]
#			listaAgentes=encontrarAgentes(meeting)
#			aux=paralelo(i, n, AgentsMeetings, NA)
#			if(aux):
#				dist=encuentraCamino(0, MeetingsDistances)
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
				aux=agent.split(':')
				AgentsMeetings[aux[0]]=aux[1]
		#Obtener y establecer las distancias entre las reuniones------------------------#
		for meetings in contentList[2].split('\n'):
			n = [int(i) for i in meetings.split() if i.isdigit()]
			if n:
				aux=meetings.split(':')
				if(len(aux[0])<=2):
					MeetingsDistances[aux[0]]=n
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
for i in AgentsMeetings:
	print(i+':'+AgentsMeetings[i])
print("---------------------")
for i in MeetingsDistances:
	print(str(i)+':'+str(MeetingsDistances[i]))
#Resolucion()
#listaFinal = [[M0,T0],[M1,T0],[M2,T1],[M3,T5]......[M_M,T_N]]
#costeFinal = 1 + 2 +3 +1 +2 +4 - 1 -1  = 11
#for i in range(0,NA)
#for n in i:
#		if(paralelo)
		#COSTEFINAL-=AC
#		costeFinal = 1 + 2 +3 +1 +2 +4 - 1 -1  = 11 DS =11
	#	CosteFinal1 = 10
	#	CosteFinal2 = 5
	#	CosteFinal3 = 11
	#	1° lo que hicimos arriba
	#	listaFinal= [10,6,8,4,5,11,11,10]
	# 	Resultado(ListaFinal, DS, ListaAgentes, AgentsMeetings, listaCoste)
	#	if(|ListaAgentes[m1] - ListaAgentes[m2]| > ListaCoste[m1-1][m2-1])
		#nota si parten en esa reunion su coste es 0
		#listafinalfinal.append(SUM(listaAgentes[Reunion_anterior]))
		#print listaFinalFinal
#if(costeFinal<=DS):
#		listaFinal.append(costeFinal)
#else:
#		 


#listaFinalFinal = [11,5 ,4 ,3 ,2 0 ,4 11, 1]