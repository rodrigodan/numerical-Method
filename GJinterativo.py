def GJ():
	# insira a ordem da matrix:
	 

	linha = 0
	coluna = 0
	acumulador = 0

	while(linha < m):
		while(coluna < n):
			if(coluna != linha):
				acumulador = acumulador + matrix[linha][coluna]
			if(matrix[linha][linha] < acumulador):
				return 0
			coluna = coluna + 1
		
		coluna = 0

		acumulador = 0

		linha = linha + 1
	return 1

def validaGJ():
	m = GJ()

	if(m == 0):

		print('pelo criterio das linhas, nao posso garantir convergencia')
		return m
	if(m == 1):
		
		print('pelo metodo de jacob, a solucao converge')
		return m


def interacaoGJ():


	for i in range(0, m):
		for j in range(0,n):
			if(i != j):
				icognitas2[i][0] = float(icognitas2[i][0] + matrix[i][j]*icognitas[j][0]) 
			if(j == (n - 1)):
				icognitas2[i][0] = (-icognitas2[i][0]/matrix[i][i]) + (coeficiente[i][0]/matrix[i][i])


	return icognitas2

def maximo():
	aux = 0
	maior = 0
	maior = abs(icognitas2[aux][0] - icognitas[aux][0])
	menor = 0
	aux = aux + 1

	while(aux < n):
		menor = abs(icognitas2[aux][0] - icognitas[aux][0])
		maior = max(maior,menor)
		aux = aux + 1
	return maior 

def criterioParada():
	if(tol > valorMaximo):
		return 1
	if(tol <= valorMaximo):
		return 0

m = input()
n = input()

# inserir cada elemento da matrix:
matrix = [[input() for x in range(m)] for y in range(n)]

if(m != n):
	print('O numero de linhas deve ser igual ao numero de coluna')

retorno = validaGJ()
if(m == n and retorno != 0):

	# cada elemento da icognita
	icognitas = [[input() for x in range(1)] for y in range(n)]

	# icognita aproximada
	icognitas2 = [[0 for x in range(1)] for y in range(n)]

	# coeficiente linear
	coeficiente = [[input() for x in range(1)] for y in range(n)]

	# valor da tolerancia
	tol = float(input())
	interacao = interacaoGJ()
	valorMaximo = maximo()
	aux2 = 0
	while(criterioParada() != 1):
		aux2 = 0
		while(aux2 < n):
			icognitas[aux2][0] = icognitas2[aux2][0]
			icognitas2[aux2][0] = 0
			aux2 = aux2 + 1

		interacao = interacaoGJ()

		# print interacao

		valorMaximo = maximo()

		# print valorMaximo
		# num = num + 1

	print('O valor da raiz aproximada com erro absoluto inferior a tolerancia dada e de:')

	print interacao



