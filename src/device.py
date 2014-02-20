# Estructura para manejar los objetos 'device'

class Device:
	def __init__(self, name, user="", fall=""):
		self.__groups = []
		self.setId(name)
		self.setUserAgent(user)
		self.setFallBack(fall)

	# Metodos Getters
	def getId(self):
		return str(self.__id)

	def getUserAgent(self):
		return str(self.__user_agent)

	def getFallBack(self):
		return str(self.__fall_back)

	def getGroups(self):
		return self.__groups

	# Metodos Setters
	def setId(self, name):
		self.__id = name

	def setUserAgent(self, user):
		self.__user_agent = user

	def setFallBack(self, fall):
		self.__fall_back = fall

	def addGroup(self, group):
		self.__groups.append(group)

	# Metodos Sobrecargados
	def __str__(self):
		salida = "Id: {0}\nUser Agent: {1}\nFall Back: {2}\n"
		return salida.format(self.getId(), self.getUserAgent(), self.getFallBack())

