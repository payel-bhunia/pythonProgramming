Pattern = [1, 1, 1, 2, 4, 8, 3, 9, 27, 4, 16, 64]
x = [i**pow for i in range(1,5) for pow in range(1,4)]
#print(x)

ans =[]
list(map(lambda x: ans.extend([x**1,x**2,x**3]),range(1,5)))
print(ans)

dic = {9:'x',2:'B',5:'C',4:'D',1:'A'}
print(dic)
t = tuple(dic)
print(dic.items())
var = list(dic.items())
print(var)
var.sort(key = lambda x: x[1])
print(var)
