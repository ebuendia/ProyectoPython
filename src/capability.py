class Capability:
	def __init__(self, name, value):
		self.setName(name)
		self.setValue(value)
		self.__group = None

	# Metodos Getters
	def getName(self):
		return str(self.__name)

	def getValue(self):
		return str(self.__value)

	def getGroup(self):
		return str(self.__group.getId())

	# Metodos Setters
	def setName(self, name):
		self.__name = name

	def setValue(self, value):
		self.__value = value

	def setGroup(self, group):
		self.__group = group

	# Metodos Sobrecargados
	def __str__(self):
		salida = "\n\t\t\tName: {0}\n\t\t\tValue: {1}"
		return salida.format(self.getName(), self.getValue())
