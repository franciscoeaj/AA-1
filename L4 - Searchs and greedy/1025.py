def busca_binaria(seq, search):    
	right = len(seq)
	left = 0
	previous_center = -1

	if search < seq[0]:
		return -1
	
	while 1:
		center = (left + right) / 2
		candidate = seq[center]
		if search == candidate:
			return seq.index(search)
		
		if center == previous_center:
			return - 2 - center
		elif search < candidate:
			right = center
		else:
			left = center
		
		previous_center = center

case = 1
while True:
	n, q = map(int, raw_input().split())

	if n == q == 0: break

	marmores = []
	for i in range(n):
		marmores.append(int(raw_input()))

	marmores = sorted(marmores)

	print "CASE# %d:" % case

	for i in range(q):
		elemento = int(raw_input())
		posicao = busca_binaria(marmores, elemento)

		if posicao < 0:
			print "%d not found" % (elemento)
		else:
			print "%d found at %d" % (elemento, posicao + 1)

	case += 1