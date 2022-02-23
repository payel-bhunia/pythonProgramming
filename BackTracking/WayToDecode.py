def decode(A):
    if len(A) == 1:
        if int(A) > 0:
            return 1
        else:
            return 0
    elif len(A) == 2:
        if int(A) > 9 and int(A) < 27:
            if int(A) == 10 or int(A) == 20:
                return 1
            else:
                return 2
        else:
            return 0
    else:
        val = (decode(A[0]) * decode(A[1:])) + (decode(A[0:2]) * decode(A[2:]))
        return val


def numDecodings(A):
    mod = 1000000007
    for i in range(len(A)):
        if A[i] == '0':
            if i == 0:
                return 0
            else:
                if A[i - 1] != '1' and A[i - 1] != '2':
                    return 0
    val = decode(A)
    return val


if __name__ == "__main__":
    A = "26101"
    print(numDecodings(A))