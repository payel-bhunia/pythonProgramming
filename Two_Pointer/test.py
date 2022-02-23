import functools
A = [1,2,3,4]
B = []
B.append(A*0)
C = [0] * 2
print(C)
print(B)
sq = [a*a for a in A]
print(sq)
summ = functools.reduce(lambda a,b: a*b, sq)
summ1 = list(map(lambda a: a*a, sq))
print(summ1)