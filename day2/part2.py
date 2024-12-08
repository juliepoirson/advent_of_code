count = 0
report = []

for line in open("input.txt").readlines():
    split_line = line.split(" ")
    report.append(split_line)

for i in range(len(report)):
    is_safe = False
    bad_level_count = 0
    if int(report[i][0]) > int(report[i][1]) and (abs(int(report[i][0]) - int(report[i][1])) <= 3):
        for x in range(1, len(report[i])-2):
            if int(report[i][x]) > int(report[i][x+1]) and (abs(int(report[i][x]) - int(report[i][x+1])) <= 3):
                is_safe = True
            else:
                is_safe = False
                if int(report[i][x-1]) > int(report[i][x+1]) and (abs(int(report[i][x-1]) - int(report[i][x+1])) <= 3):
                    bad_level_count +=1
                else:
                    break

    elif int(report[i][0]) < int(report[i][1]) and (abs(int(report[i][0]) - int(report[i][1])) <= 3):
        for x in range(1, len(report[i])-2):
            if int(report[i][x]) < int(report[i][x+1]) and (abs(int(report[i][x]) - int(report[i][x+1])) <= 3):
                is_safe = True 
            else:
                is_safe = False
                if int(report[i][x-1]) < int(report[i][x+1]) and (abs(int(report[i][x-1]) - int(report[i][x+1])) <= 3):
                    bad_level_count +=1
                else:
                    break
    print(report[i], bad_level_count)
    if is_safe == True or bad_level_count == 1:
        count += 1
    print("COUNT//", count)

print("COUNT", count)
        
