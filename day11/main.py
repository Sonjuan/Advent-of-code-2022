monkeys = []

for group in open(0).read().strip().split("\n\n") :
    lines = group.splitlines()
    monkey = []
    monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
    monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
    for line in lines[3:] :
        monkey.append(int(line.split()[-1]))
    monkeys.append(monkey)

# print(monkeys)
counts = [0] * len(monkeys)

# monkey[0] item
# monkey[1] operation
# monkey[2] test factor
# monkey[3] true target
# monkey[4] false target

# for _ in range(20) :
#     for idx, monkey in enumerate(monkeys) :
#         for item in monkey[0] :
#             item = monkey[1](item)
#             item //= 3
#             if item % monkey[2] == 0 :
#                 monkeys[monkey[3]][0].append(item)
#             else :
#                 monkeys[monkey[4]][0].append(item)
#         counts[idx] += len(monkey[0])
#         monkey[0] = []
# counts.sort()
# print(counts[-1] * counts[-2])

mod = 1
for monkey in monkeys :
    mod *= monkey[2]

for _ in range(10000) :
    for idx, monkey in enumerate(monkeys) :
        for item in monkey[0] :
            item = monkey[1](item)
            item %= mod
            if item % monkey[2] == 0 :
                monkeys[monkey[3]][0].append(item)
            else :
                monkeys[monkey[4]][0].append(item)
        counts[idx] += len(monkey[0])
        monkey[0] = []
counts.sort()
print(counts[-1] * counts[-2])