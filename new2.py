# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())
block = []
for i in range(test_case):
    block_size = int(input())
    temp = list(map(int, input().split(' ')))
    block.append(temp)
for i in range(test_case):
    last = 10000007
    start = 0
    end = len(block[i]) - 1
    flag = 0
    while start <= end:
        if block[i][start] > block[i][end]:
            max_val = block[i][start]
            min_val = block[i][end]
        else:
            min_val = block[i][start]
            max_val = block[i][end]
        if max_val <= last:
            last = max_val
        elif min_val <= last:
            last = min_val
        else:
            flag = 1
            break
        if last == block[i][start]:
            start += 1
        else:
            end -= 1
    if flag == 0:
        print('Yes')
    else:
        print("No")

    flag = 0


