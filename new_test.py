def mod_add(func):
    def insidefun1(*args):
        n = len(args)
        summ = 0
        for i in range(1,n):
            summ += args[i]
        return func(args[0],summ)
    return insidefun1

@mod_add
def add(a,b):
    return a+b


if __name__== "__main__":
    a = 2
    b = 4
    c = 3
    ans = add(a,b,c)
    print(ans)