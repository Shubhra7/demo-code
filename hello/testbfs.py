

grid=[[1,1,0,1],
      [1,0,0,1],
      [0,0,0,0]]


row = len(grid)
col = len(grid[0])
count = 0

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1):
            bfs((i,j))
            count += 1

print("The number of island present is the world: ",count)
