import re

added_up_instructions = 0
is_disabled = False

with open("input.txt", "r") as input:
	lines = input.read()
	matches = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don't\(\))", lines)
	for i in range(len(matches)):
		if matches[i][3] != '':
			is_disabled = True
		elif matches[i][2] != '':
			is_disabled = False
		if matches[i][0] != '' and matches[i][1] != '' and is_disabled == False:
			added_up_instructions += int(matches[i][0]) * int(matches[i][1])

print(added_up_instructions)