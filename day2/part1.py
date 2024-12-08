count = 0
report = []

for line in open("input.txt").readlines():
    split_line = line.split(" ")
    report.append(split_line)

for i in range(len(report)):
    is_safe = False
    if int(report[i][0]) > int(report[i][1]) and (abs(int(report[i][0]) - int(report[i][1])) <= 3):
        for x in range(len(report[i])-1):
            if int(report[i][x]) > int(report[i][x+1]) and (abs(int(report[i][x]) - int(report[i][x+1])) <= 3):
                is_safe = True
            else:
                is_safe = False
                break

    elif int(report[i][0]) < int(report[i][1]) and (abs(int(report[i][0]) - int(report[i][1])) <= 3):
        for x in range(len(report[i])-1):
            if int(report[i][x]) < int(report[i][x+1]) and (abs(int(report[i][x]) - int(report[i][x+1])) <= 3):
                is_safe = True 
            else:
                is_safe = False
                break
    if is_safe == True:
        count += 1
        
print("COUNT", count)
        
