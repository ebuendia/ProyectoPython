import re

from device import Device
from group import Group
from capability import Capability

def startDevices(line):
	return re.match(r"<devices",line.strip()) != None

def beginDevice(line):
	return re.match(r"<device",line.strip()) != None

def endDevice(line):
	return re.match(r"</device>", line.strip()) != None

def beginGroup(line):
	return re.match(r"<group", line.strip()) != None

def endGroup(line):
	return re.match(r"</group>", line.strip()) != None

def beginCapability(line):
	return re.match(r"<capability", line.strip()) != None

def endDevices(line):
	return re.match(r"</devices>", line.strip()) != None

def extractDevice(line):
	info = line.split(" ")
	return list

def deleteTags(line, tag, etag):
	return line.strip().replace(tag,"").replace(etag,"")

def getAttrId(line):
	return line.rsplit(" ")[0].replace("id=","").replace('"',"")

def getAttrUser(line):
	return line.rsplit(" ")[1].replace("user_agent=","").replace('"',"")

def getAttrFall(line):
	return line.rsplit(" ")[2].replace("fall_back=","").replace('"',"")

def getAttrName(line):
	return line.rsplit(" ")[0].replace("name=","").replace('"',"")

def getAttrValue(line):
	return line.rsplit(" ")[1].replace("value=","").replace('"',"")

def createDevices(devices):
	pass

def isTagName(s):
    """ Retorna verdadero si s es el nombre de un Tag."""
    return s[0]=='<' and s[1]!='/'

# Funcion Principal
def main():
	file = open("test.xml","r")
	line = file.readline()

	while not startDevices(line):
		line = file.readline()

	line = file.readline().strip()
	
	devices = []
	device = ""
	group = ""
	capability = ""
	while not endDevices(line):
		if beginDevice(line):
			line = deleteTags(line,"<device ",">")
			att_id = getAttrId(line)
			att_user = getAttrUser(line)
			att_fall = getAttrFall(line)
			
			device = Device(att_id, att_user, att_fall)
			line = file.readline()

		if endDevice(line):
			devices.append(device)
			line = file.readline()

		if beginGroup(line):
			line = deleteTags(line,"<group ",">")
			att_id = getAttrId(line)

			group = Group(att_id)
			group.setDevice(device)
			line = file.readline()

		if endGroup(line):
			device.addGroup(group)
			line = file.readline()

		if beginCapability(line):
			line = deleteTags(line, "<capability ", "/>")
			att_name = getAttrName(line)
			att_value = getAttrValue(line)

			capability = Capability(att_name, att_value)
			capability.setGroup(group)
			group.addCapability(capability)
			line = file.readline()

	for device in devices:
		print device

	print "Total Devices: " + str(len(devices))
	file.close()
	return 0

if __name__ == '__main__':
	main()

