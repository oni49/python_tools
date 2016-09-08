import mmap as mm

fileName = raw_input('FILE NAME: ')
f = open(fileName, 'r+b')
mem = mm.mmap(f.fileno(), 0)

def pullEncryptedKey():
	location = mem.find('encryptedKeyValue') + 19
	mem.seek(location)
	print mem.read(22) #the length of the key

def pullSaltValue():
	mem.seek(0)
	location = mem.rfind('saltValue')+11
	mem.seek(location)
	print mem.read(22)
	
pullSaltValue()