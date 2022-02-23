if __name__ == "__main__":
    n = int(input())
    vowel = set('a','e','i','o','u')
    A = []
    for i in range(n):
        s = str(input())
        A.append(s)
    for i in range(n):
        if A[i][-1] in vowel:
            print("Case #",i+1,": ",s," is ruled by Bob.")
        elif A[i][-1] == "y":
            print("Case #",i+1,": ",s," is ruled by nobody.")
        else:
            print("Case #",i+1,": ",s," is ruled by Alice.")