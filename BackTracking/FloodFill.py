def gen(image, n, m, c, x, y, p, count, total):
    # base
    #print(image)
    if count == total:
        return
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    else:
        if image[x][y] == c:
            image[x][y] = p
            gen(image.copy(), n, m, c, x + 1, y, p, count + 1, total)
            gen(image.copy(), n, m, c, x - 1, y, p, count + 1, total)
            gen(image.copy(), n, m, c, x, y + 1, p, count + 1, total)
            gen(image.copy(), n, m, c, x, y - 1, p, count + 1, total)
            #image[x][y] = c
        else:
            return


def floodFill(image, n, m, x, y, p):
    c = image[x][y]
    count = 0
    total = 0
    for i in range(n):
        for j in range(m):
            if image[i][j] == c:
                total += 1
    gen(image, n, m, c, x, y, p, count, total)
    return image


if __name__ == "__main__":
    image = [[7, 1, 1, 1],[1, 7, 7, 7],[7, 7, 7, 0],[7, 7, 7, 4],[4, 4, 4, 4]]
    n= 5
    m = 4
    x = 2
    y = 2
    p = 5
    print(floodFill(image, n, m, x, y, p))



































