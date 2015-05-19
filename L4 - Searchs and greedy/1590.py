def binary_value(val1, val2):
	bin1, bin2 = bin(val1)[2:], bin(val2)[2:]

	if len(bin1) > len(bin2):
		higher = len(bin1)
		bin2 = (len(bin1) - len(bin2)) * "0" + bin2
	else:
		higher = len(bin2)
		bin1 = (len(bin2) - len(bin1)) * "0" + bin1

	print bin1, bin2

	value = ""
	for i in range(higher):
		if int(bin1[i]) and int(bin2[i]):
			value += "1"
		else:
			value += "0"

		print bin1[i], bin2[i], bin1[i] and bin2[i], value

	print int(value, 2)

t = int(raw_input())

for case in range(t):
	n, k = map(int, raw_input().split())
	nums = map(int, raw_input().split())

	past = bin(nums[1])[2:]

	for i in range(len(nums)):
		higher = -1

		if i < len(nums) - 1:
			binary_value(nums[i], nums[i + 1]) #> higher:
				#higher = binary_value(nums[i], nums[i + 1])

	print

	#print higher