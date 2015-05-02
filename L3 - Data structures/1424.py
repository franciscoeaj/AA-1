while True:
	try:
		tamanho, consultas = map(int, raw_input().split())
		vetor = map(int, raw_input().split())
	except EOFError: break

	dicionario = {}
	for i in xrange(len(vetor)):
		if dicionario.has_key(vetor[i]):
			dicionario[vetor[i]].append(i)
		else:
			dicionario[vetor[i]] = [i]

	for i in xrange(consultas):
		ocorrencia, elemento = map(int, raw_input().split())

		if dicionario.has_key(elemento):
			if len(dicionario[elemento]) < ocorrencia:
				resultado = 0
			else: 
				resultado = dicionario[elemento][ocorrencia - 1] + 1
		else:
			resultado = 0

		print resultado