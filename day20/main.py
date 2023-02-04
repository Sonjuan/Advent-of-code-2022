#class Node :
#    def __init__(self, n) :
#        self.n = n
#        self.left = None
#        self.right = None
#
#x = [Node(int(x)) for x in open(0)]
#
#for i in range(len(x)): 
#    x[i].right = x[(i+1) % len(x)]
#    x[i].left =  x[(i-1) % len(x)]
#
#start = x[0]
#
#for k in x :
#    if k.n == 0 :
#        z = k
#        continue
#    
#    ne = k
#    offset = k.n
#
#    if(k.n == 0) :
#        z = k
#        continue
#
#    #if(k.n < 0) :
#    #    offset = k.n + len(x) -1
#    for _ in range(offset % (len(x) -1)) :
#        ne = ne.right
#
#    if(k == ne) :
#        continue
#
#    k.left.right = k.right
#    k.right.left = k.left
#    ne.right.left = k
#    k.right = ne.right
#    ne.right = k
#    k.left = ne
#    
#t = 0
#for _ in range(3) :
#    for _ in range(1000) :
#        z = z.right
#    t += z.n
#
#print(t)

class Node :
    def __init__(self, n) :
        self.n = n
        self.left = None
        self.right = None

x = [Node(int(x) * 811589153) for x in open(0)]

for i in range(len(x)): 
    x[i].right = x[(i+1) % len(x)]
    x[i].left =  x[(i-1) % len(x)]

start = x[0]

for _ in range(10) :
    for k in x :
        if k.n == 0 :
            z = k
            continue
        
        ne = k
        offset = k.n
    
        if(k.n == 0) :
            z = k
            continue
    
        #if(k.n < 0) :
        #    offset = k.n + len(x) -1
        for _ in range(offset % (len(x) -1)) :
            ne = ne.right
    
        if(k == ne) :
            continue
    
        k.left.right = k.right
        k.right.left = k.left
        ne.right.left = k
        k.right = ne.right
        ne.right = k
        k.left = ne
    
t = 0
for _ in range(3) :
    for _ in range(1000) :
        z = z.right
    t += z.n

print(t)
