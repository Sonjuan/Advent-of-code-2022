x = 1

o = []

for line in open(0):
    line = line.strip()
    if line == "noop" :
        o.append(x)
    else :
        v = int(line.split()[1])
        o.append(x)
        o.append(x)
        x += v

print(list(enumerate(o))[19::40])

print(sum(x * y +y for x, y in list(enumerate(o))[19::40]))


for i in range(0, len(o), 40) :
    for j in range(40) :
        print(end = "#" if abs(o[i+j] - j) <= 1 else " ")
    print()

