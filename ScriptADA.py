import sys
NM = 0
NA = 0
NMPA = 0
MinD = 0
MaxD = 0
DS = 0
MeetingsDistances = {}
AgentsMeetings = {}
result={}
def checkArgs(*args):
	if len(sys.argv) < 2:
		print("ERROR: Instancia no especificada")

def crearArray(dato):
	listaAux = []
	for i in dato:
		listaAux.append(int(i))
	return listaAux
def encuentraCoste(meeting1,meeting2):
	meetingsPath=0
	if(meeting1!=meeting2):
		m1=MeetingsDistances[meeting1]
		meetingsPath+=m1[meeting2]+1
	return meetingsPath	
def paralelo(j, agenteA, agenteB):#numero>0
	noAtiendenAmbos = True
	if(agenteA!=agenteB):
		a0=AgentsMeetings[agenteA]
		a1=AgentsMeetings[agenteB]
		if(a0[j]!=a1[j]):
			noAtiendenAmbos=False
	return noAtiendenAmbos
def encontrarAgentes(meeting):
	retorno=list()
	for i in AgentsMeetings:
		if(meeting in AgentsMeetings[i]):
			retorno.append(i)
	return retorno
"""def comprobacion(agenteB):
	retorno=True
	total=0
	a1=AgentsMeetings[agenteB]
	for j in range(1,len(a1)):
		for i in AgentsMeetings:
			if(agenteB!=i):
				if(paralelo(j,agenteB,i)):
					total-=1
		if(j<len(a1)-1):
			total+=encuentraCoste(a1[j],a1[j+1])
	print(total)
	if(total>DS):
		retorno=False
	return retorno"""
def orden():
	aux={}
	repetidos={}
	unicos={}
	for i in AgentsMeetings:
		aux[i]=AgentsMeetings[i]
	count=1
	for i in aux:
		test=encontrarAgentes(count)
		if(len(test)>1):
			repetidos[count]=test
		else:
			unicos[count]=test
		count+=1
	result[0]=unicos
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
				AgentsMeetings[aux[0]]=n
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
	except:
		print("ERROR: Instancia no encontrada")

checkArgs()
test=getNumbers(sys.argv[1])

NM= test[0]
NA= test[1]
NMPA= test[2]
MinD= test[3]
MaxD= test[4]
DS= test[5]
orden()
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