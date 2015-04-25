while True:
	try:
		line = raw_input()
	except EOFError: break

	pos = 0
	o_pos = 0
	output_letters = []
	while True:
		if pos == len(line) - 1: break

		if line[pos] == "[":
			o_pos = 0
		elif line[pos] == "[":
			o_pos = len(line) - 1
		else:
			o_pos = pos

		pos += 1

		output_letters.insert(o_pos, line[pos])

	output = ""
	for i in range(len(output_letters)):
		output += output_letters[i]

	print output