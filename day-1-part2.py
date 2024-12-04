list_a = []
list_b = []
count = 0
sim_score = 0

for line in open("day-1.txt").readlines():
    split = line.split()
    list_a.append(split[0])
    list_b.append(split[1])


for i in list_a:
    for x in list_b:
        if i == x:
            count += 1

    sim_score += count * int(i)
    count = 0

print(sim_score)
    