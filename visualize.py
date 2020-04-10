import matplotlib.pyplot as plt
import numpy as np
#f = open("successVSagents","r")
f = open("runtimeVSagents","r")
x = np.zeros(5)
y1 = np.zeros(5)
y2 = np.zeros(5)

#agents,CBS,CBSH
i = 0
for s in f:
	inp = s.split(',')
	x[i] = float(inp[0])
	y1[i] = float(inp[1])
	y2[i] = float(inp[2])
	i += 1

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("#Agents")
#plt.ylabel("success(ms)")
plt.ylabel("runtime(ms)")
plt.show()
