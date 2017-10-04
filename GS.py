def interacaoGS():

	k = 0
	for i in range(0, m):
		for j in range(0,n):
			if(i != j):
				# print icognitas2[i][0]
				icognitas2[i][0] = float(icognitas2[i][0] + abs(matrix[i][j])*icognitas[k][0]) 


				k += 1
				
			if(j == (n - 1)):
				icognitas2[i][0] = float(icognitas2[i][0]/abs(matrix[i][i]))
				icognitas[i][0] = icognitas2[i][0]
				# icognitas2[i][0] = 0
				k = 0
		
	return icognitas


def maximo():
	i = 0
	maior = icognitas[i][0]
	i += 1
	while(i < n):
		maior = max(maior, icognitas[i][0])
		i += 1
	return maior


def converge():
	if(maximo() < 1):
		print ('converge')
	if(maximo() >= 1):
		print ('nao passou no criterio de convergencia de Gaus-Seidel')

#insira os elementos da matrix:
m = input()
n = input()

# inserir cada elemento da matrix:
matrix = [[input() for x in range(m)] for y in range(n)]

icognitas = [[1 for x in range(1)] for y in range(n)]

icognitas2 = [[0 for x in range(1)] for y in range(n)]


interacaoGS()


# jj = 0
# while(jj < m):
# 	print icognitas[jj][0]
# 	jj += 1

converge()