# v = set([(0, 0)])

# H = [0, 0]
# T = [0, 0]


# for line in open(0):
#     a, b = line.split()
#     b = int(b)
#     for _ in range(b):
#         dx = 1 if a == "R" else -1 if a == "L" else 0
#         dy = 1 if a == "U" else -1 if a == "D" else 0

#         H[0] += dx
#         H[1] += dy

#         _x = H[0] - T[0]
#         _y = H[1] - T[1]


#         if abs(_x) > 1 or abs(_y) > 1:
#             if _x == 0:
#                 T[1] += _y // 2
#             elif _y == 0:
#                 T[0] += _x // 2
#             else:
#                 T[0] += 1 if _x > 0 else -1
#                 T[1] += 1 if _y > 0 else -1
        
#         v.add(tuple(T))

# print(len(v))

v = set([(0, 0)])

R = [[0, 0] for _ in range(10)]
# note R = [0, 0] * 10 makes point-everylist-array

for line in open(0):
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        R[0][0] += dx
        R[0][1] += dy

        for i in range(9):
            H = R[i]
            T = R[i + 1]

            _x = H[0] - T[0]
            _y = H[1] - T[1]

            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    T[1] += _y // 2
                elif _y == 0:
                    T[0] += _x // 2
                else:
                    T[0] += 1 if _x > 0 else -1
                    T[1] += 1 if _y > 0 else -1

        v.add(tuple(R[-1]))

print(len(v))