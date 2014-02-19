class Group:
	def __init__(self, group):
		setId(group)
		self.__device = ""
		self.__capabilities = []

	# Metodos Getters
	def getId(self):
		return str(self.__id)

	def getDevice(self):
		return str(self.__device)

	def getCapabilities(self):
		return str(self.__capabilities)

	# Metodos Setters
	def setId(self, group):
		self.__id = group

	def setDevice(self, device):
		self.__device = device

	def setCapability(self, capability):
		self.__capabilities.append(capability)

	# Metodos Sobrecargados
	def __str__(self):
		salida = "Id: {0}\n"
		return salida.format(self.getId())
