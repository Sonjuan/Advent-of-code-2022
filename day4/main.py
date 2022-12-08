# result = 0
# while True :
#     try :
#         line = input()
#     except :
#         break

#     a1,a2,b1,b2 = [int(x) for x in line.replace(",", "-").split("-")]
#     if((a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2)) :
#         result += 1 
# print(result)

result = 0
while True :
    try :
        line = input()
    except :
        break
    
    a1,a2,b1,b2 = [int(x) for x in line.replace(",", "-").split("-")]
    if((a1 <= b1 and b1 <= a2) or (b1 <= a1 and a1 <= b2)) :
        result += 1 

print(result)
# set(range(a, b+1)) & set(range(x, y+1))