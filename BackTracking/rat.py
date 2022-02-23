def gen_path(maze, n, i, j, curr, ans):
    # base
    if i == n - 1 and j == n - 1:
        curr.append([i, j])
        ans.append(curr)
        return
    else:
        if (i >= n or i < 0) or (j >= n or j < 0):
            return
        else:
            if maze[i][j] == 0:
                return
            else:
                maze[i][j] = 0
                curr.append([i, j])
                gen_path(maze.copy(), n, i + 1, j, curr.copy(), ans)
                gen_path(maze.copy(), n, i - 1, j, curr.copy(), ans)
                gen_path(maze.copy(), n, i, j + 1, curr.copy(), ans)
                gen_path(maze.copy(), n, i, j - 1, curr.copy(), ans)
                maze[i][j] = 1
                curr.pop()


def ratInAMaze(maze, n):
    # Write your code here.
    i = 0
    j = 0
    ans = []
    curr = []
    gen_path(maze, n, i, j, curr, ans)
    res = []
    leng = len(ans)
    for i in range(leng):
        rows, cols = (n, n)
        final = list([[0 for i in range(cols)] for j in range(rows)])
        # final = [[0 for i in range(n)] for j in range(n)]
        for j in ans[i]:
            row = j[0]
            col = j[1]
            final[row][col] = 1

        for i in range(n):
            for j in range(n):
                print(final[i][j], end=' ')
        print()


# Main.
n = int(input())
maze = n * [0]

for i in range(0, n):
    maze[i] = input().split()
    maze[i] = [int(j) for j in maze[i]]

ans = ratInAMaze(maze, n)