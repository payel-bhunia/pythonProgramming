def solve(a):
    if a < 0:
        print("it is not pallindrome")
    elif a == 0:
        print("it is pallindrome")
    b = a
    s = ''
    while b > 0:
        s = s + str(b % 10)
        b = b // 10

    if int(s) == a:
        print("it is pallindrome")
    else:
        print("it is not pallindrome")


if __name__ == '__main__':
    A = 12321
    solve(A)


