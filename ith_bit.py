x = 127
count = 0
while x > 0:
    if x & 1 == 1:
        count += 1
        x = x >> 1
print(count)
