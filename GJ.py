def GJ():
	# insira a ordem da matrix:
	m = input()
	n = input()

	# inserir cada elemento da matrix:
	matrix = [[input() for x in range(m)] for y in range(n)] 

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

		print('pelo metodo de jacob, nada pode dizer')

	if(m == 1):
		
		print('pelo metodo de jacob, a solucao converge')

validaGJ()
