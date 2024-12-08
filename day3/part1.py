import re

added_up_instructions = 0

with open("input.txt", "r") as input:
	lines = input.read()
	x = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", lines)

	for i in range(len(x)):
		added_up_instructions += int(x[i][0]) * int(x[i][1])
	print(added_up_instructions)