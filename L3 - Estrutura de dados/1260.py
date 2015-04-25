n = int(raw_input())
blank = raw_input()

for i in range(n):
	species = {}
	total = 0
	while True:
		try:
			specie = raw_input()
		except EOFError: break
		if len(specie) == 0: break

		if species.has_key(specie):
			species[specie] += 1
		else:
			species[specie] = 1

		total += 1

	if i > 0: print ""

	keys = sorted(species.keys())
	for k in range(len(keys)):
		print "%s %.4f" % (keys[k], 100.0 * species.get(keys[k]) / total)