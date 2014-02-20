class Capability:
	def __init__(self, name, value):
		self.setName(name)
		self.setValue(value)
		self.__group = ""

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
		salida = "Name: {0}\nValue: {1}\n"
		return salida.format(self.getName(), self.getValue())
