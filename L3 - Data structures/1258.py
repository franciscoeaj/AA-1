def get_tamanho_camiseta(i):
	if i == 0:
		tamanho = "P"
	elif i == 1:
		tamanho = "M"
	else:
		tamanho = "G"

	return tamanho

n = int(raw_input())
while True:
	if n == 0: break

	brancas, vermelhas = [[], [], []], [[], [], []]
	for i in range(n):
		nome = raw_input()
		cor, tamanho = map(str, raw_input().split())

		if cor == "branco":
			if (tamanho == "P"):
				brancas[0].append(nome)
			elif (tamanho == "M"):
				brancas[1].append(nome)
			else:
				brancas[2].append(nome)
		else:
			if (tamanho == "P"):
				vermelhas[0].append(nome)
			elif (tamanho == "M"):
				vermelhas[1].append(nome)
			else:
				vermelhas[2].append(nome)

	for i in range(len(brancas)):
		tamanho = get_tamanho_camiseta(i)

		for j in range(len(brancas[i])):
			brancas_ordenada = sorted(brancas[i])
			print "branco", tamanho, brancas_ordenada[j]

	for i in range(len(vermelhas)):
		tamanho = get_tamanho_camiseta(i)

		for j in range(len(vermelhas[i])):
			vermelhas_ordenada = sorted(vermelhas[i])
			print "vermelho", tamanho, vermelhas_ordenada[j]

	n = int(raw_input())

	if n != 0: print ""