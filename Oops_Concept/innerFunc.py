def computeDeviceCrossovers(n, websiteVisits, m, appVisits):
    # Write your code here
    if m == 0 or n == 0:
        return 0
    else:
        i = 0
        j = 0
        count = 0
        flag = 0
        while i < n and j < m:
            if websiteVisits[i] < appVisits[j]:
                i += 1
                if flag == 1:
                    count += 1
                    flag = 0
            else:
                if flag == 0:
                    if j != 0:
                        count += 1
                    flag = 1
                j += 1
        if i < n or j < m:
            count += 1
        return count


n = int(input())
websiteVisits = []
appVisits = []
for i in range(n):
    temp = int(input())
    websiteVisits.append(temp)
m = int(input())
for i in range(m):
    temp = int(input())
    appVisits.append(temp)

out_ = computeDeviceCrossovers(n, websiteVisits, m, appVisits)
print(out_)