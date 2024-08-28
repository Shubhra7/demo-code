
import collections

q= collections.deque()
visited = set()
directions = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j):
    visited.add((i,j))
    q.append((i,j))
    while q:
        r,c = q.popleft()
        for m,n in directions:
            ro = r + m
            co = c + n
            if(ro in range(row) and co in range(col)
               and grid[ro][co]==1 and (ro,co) not in visited):
                q.append((ro,co))
                visited.add((ro,co))




grid=[[1,1,0,1],
      [1,0,0,1],
      [0,0,0,0]]


row = len(grid)
col = len(grid[0])
count = 0

for i in range(row):
    for j in range(col):
        if(grid[i][j]==1 and (i,j) not in visited):
            bfs(i,j)
            count += 1

print("The number of island present is the world: ",count)
