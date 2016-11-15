import csv

# with open('logdummy.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		print ', '.join(row)
with open('logdummy.csv', 'rb') as csvfile:
	data=[]
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		data.append(', '.join(row))
print len(data)
def dataCleansing(log, unneeded):
	clean=[]
	for i in range(1,10):
		for un in unneeded:
			if((' ' + log[i] + ' ') in (' ' + un + ' ')):
				clean.append(log[i])
			else:
				print("sdjdjsk")
	return clean

mustDel=['gif','JPEG','JPG']
print dataCleansing(data,mustDel)