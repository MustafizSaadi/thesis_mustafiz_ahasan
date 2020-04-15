import matplotlib.pyplot as plt
import numpy as np
#f = open("successVSagents","r")
#f = open("runtimeVSagents","r")
f = open("costVSagents","r")
x = np.zeros(8)
y1 = np.zeros(8)
y2 = np.zeros(8)
#y3 = np.zeros(6)

#agents,CBS,CBSH,pibt
i = 0
for s in f:
	inp = s.split(',')
	x[i] = float(inp[0])
	y1[i] = float(inp[1])
	y2[i] = float(inp[2])
#	y3[i] = float(inp[3])
	i += 1

fig,ax = plt.subplots()

ax.plot(x,y1,label='CBS(ID)')
#ax.plot(x,y2,label='CBSH-WDG')
ax.plot(x,y2,label='PIBT')


ax.legend()

plt.xlabel("#Agents")
#plt.ylabel("runtime(ms)")
plt.ylabel("Sum of costs")
plt.show()
