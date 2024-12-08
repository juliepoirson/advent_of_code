import regex as re

horizontal_input = []
vertical_input = []
diag_right_input = []
diag_left_input = []

rev_diag_right_input = []
rev_diag_left_input = []

count = 0

# horizontal input
for line in open("input.txt").readlines():
    input_line = line.strip()
    horizontal_input.append(input_line)

num_lines = len(horizontal_input)
line_length = len(horizontal_input[0])

for line in range(num_lines):
    for letter in range(line_length):
        if line == 0:
            # vertical input
            vertical_input.append(horizontal_input[line][letter])
            # diagonal input
            diag_right_input.append(horizontal_input[line][letter])
            diag_left_input.append(horizontal_input[line][letter])
        else:
            # vertical input
            vertical_input[letter] += horizontal_input[line][letter]
            # diagonal input
            if letter != (line_length-1) and line+letter < line_length:
                diag_right_input[letter] += horizontal_input[line][line+letter]
            if letter != (line_length-1) and line+letter < line_length:
                diag_left_input[line+letter] += horizontal_input[line][letter]

# code for the rest of the diagonals that weren't captured since they start on the last line
for line in range(num_lines-1, -1, -1):
    for letter in range(line_length):
        if line == len(horizontal_input)-1:
            rev_diag_right_input.append(horizontal_input[line][letter])
            rev_diag_left_input.append(horizontal_input[line][letter])
        else:
            if letter != (line_length-1) and (letter+((num_lines-1)-line)) < line_length:
                rev_diag_left_input[letter+((num_lines-1)-line)] += horizontal_input[line][letter]
            if letter != (line_length-1) and (letter+((num_lines-1)-line)) < line_length:
                rev_diag_right_input[letter] += horizontal_input[line][letter+((num_lines-1)-line)]

# Knowing the input is a square, meaning the number of char in one line is equal to the number of lines, 
# I decided to only handle that case scenario and not the case where the diagonals start neither on the first 
# or last line just for efficient completion of the coding problem. 
if line_length == num_lines:
    rev_diag_left_input.pop(len(rev_diag_left_input)-1)
    rev_diag_right_input.pop(0)

# checking if XMAS is in the strings in the different lists
total_input = horizontal_input + vertical_input + diag_left_input + diag_right_input + rev_diag_left_input + rev_diag_right_input
for string in total_input:
    xmas1 = re.findall(r"(XMAS|SAMX)", string, overlapped=True)
    count += len(xmas1)

print(count)