def main():
    arr = [5, 1, 2, 8]
    n = 9
    for i in range(4):
        arr[i] = arr[i] * n

    for i in range(4):
        ind = arr[i] // n
        y = arr[ind] // n
        arr[i] += y
    print(arr)

    for i in range(4):
        arr[i] = arr[i] % n
    print(arr)


if __name__ == "__main__":
    main()

