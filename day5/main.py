import re

s =[]
x = open(0)
for line in x :
    if line == "\n" :
        break
    s.append(list(line[1::4]))
s.pop()

s = [list("".join(c).strip()[::-1]) for c in zip(*s)]
print(s)

for line in x :
    a, b, c = [int(x) for x in re.findall("\\d+", line)]
    print(a,b,c)
    s[c-1].extend(s[b-1][-a:])
    s[b-1] = s[b-1][:-a]
print(s)
print("".join(x[-1] for x in s))