def main():
    with open('input.txt') as f:
        contents = f.read()

    output1, output2 = contents.split('\n\n')

    ordering_rules_input = output1.split()
    updates_input = output2.split()

    ordering_rules = {}

    # dictionary
    for rule in ordering_rules_input:
        number = rule.split("|")
        if number[0] in ordering_rules:
            ordering_rules[number[0]].append(number[1])
        else:
            ordering_rules[number[0]] = [number[1]]

    middle_num_total = 0

    for update in updates_input:
        line = update.split(",")
        if is_order_correct(line, ordering_rules):
            line_middle = len(line) // 2
            middle_num_total += int(line[line_middle])

    print(f"Part 1 answer: {middle_num_total}")

def is_order_correct(line: list[str], ordering_rules: dict[str, list[str]]) -> bool:
    for num in line:
        if num in ordering_rules:
            for x in ordering_rules[num]:
                if x in line and not line.index(num) < line.index(x):
                    return False
    return True

if __name__ == "__main__":
    main()