import socket

file = open('prettyLog.txt', 'r')
outFile = open('domainList.txt', 'w')

ipList = []
for line in file.readlines():
	src = ''
	dpt = ''
	spt = ''
	proto = ''
	for x in line.split():
		if 'SRC=' in x:
			 src = x.split('=')[1]
		elif 'DPT=' in x:
			dpt = x.split('=')[1]
		elif 'SPT=' in x:
			spt = x.split('=')[1]
		elif 'PROTO=' in x:
			proto = x.split('=')[1]
	if len(src)>0:
		ipList.append((src, dpt, spt, proto))

# print ipDict.keys()[1], socket.gethostbyaddr(ipDict.keys()[1]), ipDict[ipDict.keys()[1]]
for entry in ipList:
	try:
		nslook = socket.gethostbyaddr(entry[0])
		domain = nslook[0]
		alias = nslook[1]
		altIPs = nslook[2]
	except Exception, e:
		domain = 'unknown'
		alias = 'unknown'
		altIPs = 'unknown'
	outFile.write(domain+'\t'+entry[0]+'\t'+str(alias)+'\t'+str(altIPs)+'\t'+entry[1]+'\t'+entry[2]+'\t'+entry[3]+'\n')
	print domain, entry[0], alias, altIPs, entry[1:3]
	
outFile.close()
file.close()