import sys
NM = 0
NA = 0
NMPA = 0
MinD = 0
MaxD = 0
DS = 0
MeetingsDistances = {}
Agents = []
AgentsMeetings = {}
result=list()
Instance = sys.argv[1]
def checkArgs(*args):
	if len(sys.argv) < 2:
		print("ERROR: Instancia no especificada")

def crearArray(dato):
	listaAux = []
	for i in dato:
		listaAux.append(int(i))
	return listaAux

def getDistanceBetween(m1,m2):
	return MeetingsDistances[m1][m2]

def paralelo(j, agentA, agentB):#numero>0
	return AgentsMeetings[agentA][j] == AgentsMeetings[agentB][j]

def truncar(agent):
	meetings = AgentsMeetings[agent]
	NumberOfMeetings = len(meetings)
	aux = 1
	for i in range(0, NumberOfMeetings):
		private = True
		for j in AgentsMeetings:
			if(j != agent):
				if(meetings[i] in AgentsMeetings[j]):
					private = False
		if not private:
			aux +=1
		else: break
	if (aux > NumberOfMeetings):
		aux = NumberOfMeetings
	timeslots = aux
	print("aux: ", aux)
	for j in range(0, aux):
		if(j < aux - 1):
			timeslots += getDistanceBetween(meetings[j], meetings[j+1])
	return timeslots

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
def Solve(NM, NA, NMPA, MinD, MaxD, DS, MeetingsDistancess, AgentsMeetings):
	return 0
def getNumbers(Instancia): #Función dedicada a obtener los datos del MSP
#	try:
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
				AgentsMeetings[aux[0]] = n
#				AgentsMeetings[int(aux[0])]=aux[1].split(' ')
		#Obtener y establecer las distancias entre las reuniones------------------------#
		for meetings in contentList[2].split('\n'):
			n = [int(i) for i in meetings.split() if i.isdigit()]
			if n:
				aux=meetings.split(':')
				if(len(aux[0])<=2):
					MeetingsDistances[int(aux[0])]=n
		file.close()
		return PrettyNumbers
		#-------------------------------------------------------------------------------#
#	except:
#		print("ERROR: Instancia no encontrada")
checkArgs()
test = getNumbers(Instance)
NM= test[0]
NA= test[1]
NMPA= test[2]
MinD= test[3]
MaxD= test[4]
DS= test[5]
# Agente 0: tiempo en las reuniones + tiempo entre reuniones - casos paralelos
# Agente 0: 5 + 6 - 8 = 3
print(truncar("Agents (0)"))

#print(DS)
#for i in AgentsMeetings:
#	print(comprobacion(i))
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