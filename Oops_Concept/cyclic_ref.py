# Python program to illustrate destructor

class A:
    def __init__(self, bb):
        self.b = bb
        print(self.b)
    def __del__(self):
        print("die1")

class B:
    def __init__(self):
        #self.a = A(self)
        print('here')

    def __del__(self):
        print("die")

class C:
    def __del__(self):
        print("die2")

def fun():
    b = B()
    obj = A(b)
    obc = C()


fun()
x = [1,2,3]
y = [4,5,6]
x.append(y)
y.append(x)
print(x,y)
del x
print(y)