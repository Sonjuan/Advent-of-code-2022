for x in open(0) :
    s = []
    for idx, c in enumerate(x) :
        s.append(c)
        if len(s) == 14 :
            if len(s) == len(set(s)):
                print(idx+1)
            else :
                s = s[1:]