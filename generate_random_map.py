import numpy as np

obstacle_density = 0.3
dim = 200
a = []
out = open("output.txt","a")
for i in range(dim):
	a.append(['.'] * dim)

#cnt = 0

for i in range(dim):
	for j in range(dim):
		val=np.random.random_sample()
		if val <= obstacle_density:
			a[i][j] = '@'
			#cnt += 1
			

for i in range(dim):
	s = ""
	for j in range(dim):
		s += a[i][j]
	out.write(s + '\n')

out.close()

#print(cnt)
