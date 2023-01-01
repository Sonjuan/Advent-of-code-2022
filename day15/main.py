#import re
#
#pattern = re.compile(r"-?\d+")
#Y = 2000000
#meet = set()
#intervals = []
#
#for line in open(0) :
#    sx, sy, bx, by = map(int, pattern.findall(line))
#    r = abs(sx - bx) + abs(sy - by)
#    d = abs(sy - Y)
#
#    if r - d < 0 :
#        continue
#
#    if by == Y :
#        meet.add(bx)
#
#    lx = sx - (r - d)
#    hx = sx + (r - d)
#
#    intervals.append((lx, hx))
#
#intervals.sort()
#q = []
#
#for lo, hi in intervals :
#    if not q :
#        q.append([lo, hi])
#        continue
#
#    qlo, qhi = q[-1]
#
#    if lo > qhi + 1 :
#        q.append([lo, hi])
#        continue
#    
#    q[-1][1] = max(qhi, hi)
#
#cannot = set()
#
#for lo, hi in q :
#    for x in range(lo, hi + 1) :
#        cannot.add(x)
#
#print(len(cannot - meet))

import re

pattern = re.compile(r"-?\d+")
lines = [list(map(int, pattern.findall(line))) for line in open(0)]
M = 4000000

for Y in range(M+1) :
    intervals = []

    for sx, sy, bx, by in lines :
        r = abs(sx - bx) + abs(sy - by)
        d = abs(sy - Y)

        if r - d < 0 :
            continue

        lx = sx - (r - d)
        hx = sx + (r - d)

        intervals.append((lx, hx))

    intervals.sort()
    q = []

    for lo, hi in intervals :
        if not q :
            q.append([lo, hi])
            continue

        qlo, qhi = q[-1]

        if lo > qhi + 1 :
            q.append([lo, hi])
            continue
    
        q[-1][1] = max(qhi, hi)

    x = 0

    for lo, hi in q :
        if x < lo :
            print(x * 4000000 + Y)
            exit(0)
        x = max(x, hi + 1)
        if x > M :
            break


# there is only 1 valid point
# checking permiter of sensors
# iterating sensor's radiant+1 and compare points to other sensor's distance




