class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # guards = 1, walls = 2, guardable = 3
        # mark as guards 
        for r,c in guards:
            grid[r][c] = 1 
        for r, c in walls:
            grid[r][c] = 2 
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in [1,2]:
                        break 

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc 
            
        unguarded_count = 0 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1
        return unguarded_count



        