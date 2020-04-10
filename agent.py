import random
#n = input("Enter number of agents\n")
f = open("output2.txt","r")
#out = open("agents"+n,"a")
out = open("agents11","a")
#out.write(n+"\n")
a = []
for s in f:
	a.append(s)
#for i in range(int(n)):
#	while True:
#		strow=random.randrange(0,len(a))
#		stcol=random.randrange(0,len(a))
#		if a[strow][stcol]!='@':
#			out.write(str(strow)+","+str(stcol))
#			break
#	while True:
#		goalrow=random.randrange(0,len(a))
#		goalcol=random.randrange(0,len(a))
#		if a[goalrow][goalcol]!='@':
#			out.write(","+str(goalrow)+","+str(goalcol)+",\n")
#			break

for i in range(10):
	while True:
		strow=random.randrange(0,len(a))
		stcol=random.randrange(0,len(a))
		if a[strow][stcol]!='@':
			out.write(str(strow)+","+str(stcol))
			break
	while True:
		goalrow=random.randrange(0,len(a))
		goalcol=random.randrange(0,len(a))
		if a[goalrow][goalcol]!='@':
			out.write(","+str(goalrow)+","+str(goalcol)+",\n")
			break
