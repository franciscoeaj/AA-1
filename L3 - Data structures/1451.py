while True:
	try:
		line = raw_input()
	except EOFError: break

	home_text_list = []
	end_text = ""
	home_pressed = False
	for letter in line:
		if letter == "[":
			home_pressed = True
			home_text_list.append("")
		elif letter == "]":
			home_pressed = False
		else:
			if home_pressed:
				home_text_list[-1] += letter
			else:
				end_text += letter

	home_text = ""
	for i in range(len(home_text_list) - 1, -1, -1):
		home_text += home_text_list[i]

	print home_text + end_text