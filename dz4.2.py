lst=[0, 1, 7, 2, 4, 8]
if len(lst) > 0:
 plus=sum(lst[a] for a in range(0, len(lst), 2))
 print(plus * lst[-1])
else:
    plus = 0
    print(plus)
