while True:
	try:
		line = raw_input()
	except EOFError: break

	home_text_list = []
	end_text = ""
	middle_text = ""
	current_text = ""
	pressed_key = -1			# -1 for none, 0 for home, 1 for end
	home_count = 0
	for i in range(len(line)):
		if line[i] == "[":
			pressed_key = 0
			home_count += 1

		if line[i] == "]":
			pressed_key = 1

		if line[i] != "[" and line[i] != "]":
			if pressed_key == 1:
				end_text += line[i]
			elif pressed_key == 0:
				current_text += line[i]
				if i < len(line) - 1 and line[i + 1] == "]":
					if home_count > 1:
						home_text_list.insert(0, current_text)
					else:
						home_text_list.append(current_text)

					current_text = ""
				
				if i == len(line) - 1:
					home_text_list.insert(0, current_text)

			else:
				middle_text += line[i]

	home_text = ""
	for i in range(len(home_text_list)):
		home_text += home_text_list[i]

	print home_text + middle_text + end_text