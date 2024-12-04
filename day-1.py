list_a = []
list_b = []
diff = 0

for line in open("day-1.txt").readlines():
    split = line.split()
    list_a.append(split[0])
    list_b.append(split[1])

list_a.sort()
list_b.sort()


for i in range(len(list_a)):
    diff += abs(int(list_a[i]) - int(list_b[i]))

print(diff)
    