import numpy as np
f = open("input.txt","r")
st = []
gl = []
agent = 0
for s in f:
	inp = s.split(',')
	st.append((int(inp[0]),int(inp[1])))
	gl.append((int(inp[2]),int(inp[3])))
	agent += 1
dim = 4
#env = np.zeros((dim,dim,2))
for id in range(1):
	for density in [0,.1,.2,.3]:
		env = np.zeros((2,dim,dim))
		fstr = str(agent)+"_agents_"+str(dim)+"_size_"+str(density)+"_density_id_"+str(id)+"_environment.npy"
		f = open(fstr,"w")
		for val in st:
			env[0][val[0]][val[1]] = st.index(val) + 1
		for val in gl:
			env[1][val[0]][val[1]] = gl.index(val) + 1
		for i in range(dim):
			for j in range(dim):
				prob = np.random.random_sample()
				if(prob<density and not env[0][i][j] and not env[1][i][j]):
					env[0][i][j] = -1 	
		np.save(fstr,env)
