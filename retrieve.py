f = open("test")
out = open("output.txt","a")
dim = 32
a = []
for i in range(dim):
	a.append(['.'] * dim)

for s in f:
	temp = s[7:-2]
	digit = temp.split(', ')
	d1 = digit[0]
	d2 = digit[1]
	a[int(d1)][int(d2)] = '@'

for i in range(dim):
	s = ""
	for j in range(dim):
		s += a[i][j]
	out.write(s + '\n')
