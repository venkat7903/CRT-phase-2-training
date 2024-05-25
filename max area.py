def maxAreaOfIsland(grid):
        m = len(grid)
        n = len(grid[0])
        one_list = []
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    one_list.append([i, j])
        
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        q = one_list.copy()
        
        while len(q) > 0:
            area=0
            for i in range(len(q)):
                print(q)
                r, c = q.pop(0)
                for ro, co in d:
                    row = ro + r
                    col = co + c
                    if row < 0 or col < 0 or row >= m or col >= n or [row, col] not in one_list:
                        continue
                    q.append([row, col])
                    area += 1
                    one_list.remove([row, col])
            if max_area < area:
                max_area = area
        return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))