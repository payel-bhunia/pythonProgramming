def func(a=9,b=10):
    print('a=',a)
    print('b=',b)

def fun2(**kwarg):
    for key,values in kwarg.items():
        print(key,values)


func()
dic = {'x':11, 'b':12}
fun2(**dic)
