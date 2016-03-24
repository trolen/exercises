import sys
with open('snowman.dat','r') as f:
	D=f.read().split('|')
def d(n):
	return D[4*n+int(sys.argv[1][n])-1]
print ' '+d(0)[:5]+'\n '+d(0)[5:]+'\n'+d(4)[0]+'('+d(2)+d(1)+d(3)+')'+d(5)[0]+'\n'+d(4)[1]+'('+d(6)+')'+d(5)[1]+'\n ('+d(7)+')\n'
