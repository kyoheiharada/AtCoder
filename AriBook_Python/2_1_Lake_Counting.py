n = 10
m = 12
field = [["W", ".", ".", ".", ".", ".", ".", ".", ".", "W", "W", "."],
         [".", "W", "W", "W", ".", ".", ".", ".", ".", "W", "W", "W"],
         [".", ".", ".", ".", "W", "W", ".", ".", ".", "W", "W", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "W", "W", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", "."],
         [".", ".", "W", ".", ".", ".", ".", ".", ".", "W", ".", "."],
         [".", "W", ".", "W", ".", ".", ".", ".", ".", "W", "W", "."],
         ["W", ".", "W", ".", "W", ".", ".", ".", ".", ".", "W", "."],
         [".", "W", ".", "W", ".", ".", ".", ".", ".", ".", "W", "."],
         [".", ".", "W", ".", ".", ".", ".", ".", ".", ".", "W", "."]]


def dfs(x, y):
    field[x][y] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == "W":
                dfs(nx, ny)


res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == "W":
            dfs(i, j)
            res += 1

print(res)
