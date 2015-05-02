def maior(lista):
	maior = lista[0]
	for i in range(1, len(lista)):
		if lista[i] > maior:
			maior = lista[i]

	return maior

n = int(raw_input())

for caso_teste in range(n):
	l = int(raw_input())
	vagoes = map(int, raw_input().split())

	swaps = 0
	for i in range(len(vagoes)):
		maior_vagao = maior(vagoes)
		swaps += len(vagoes) - 1 - vagoes.index(maior_vagao)
		vagoes.remove(maior_vagao)

	print "Optimal train swapping takes %d swaps." % (swaps)