# result = 0

# for line in open(0) :
#     x = len(line) // 2
#     a = line[:x]
#     b = line[x:]
#     k, = set(a) & set(b)
#     if k >= "a" :
#         result += ord(k) - ord("a") +1
#     else :
#         result += ord(k) - ord("A") + 27

# print(result)

result = 0

while True :
    try :
        x = input()
        y = input()
        z = input()
    except:
        break

    k, = set(x) & set(y) & set(z)
    if k >= "a" :
        result += ord(k) - ord("a") +1
    else :
        result += ord(k) - ord("A") + 27

print(result)