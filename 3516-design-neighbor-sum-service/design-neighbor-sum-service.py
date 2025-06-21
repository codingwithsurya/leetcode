class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])

        self.adj_offsets = [(-1,0), (1,0), (0,-1), (0,1)]
        self.diag_offsets = [(-1, -1), (-1, 1), (1, -1), (1,1)]

    def _in_bounds(self, r, c):
        return 0 <= r < self.ROWS and 0 <= c < self.COLS
    def adjacentSum(self, value: int) -> int:
        adj_sum = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.grid[r][c] == value:
                    for dr, dc in self.adj_offsets:
                        nr, nc = r + dr, c + dc 
                        if self._in_bounds(nr,nc):
                            adj_sum += self.grid[nr][nc]
        return adj_sum

    def diagonalSum(self, value: int) -> int:
        diag_sum = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.grid[r][c] == value:
                    for dr, dc in self.diag_offsets:
                        nr, nc = r + dr , c + dc 
                        if self._in_bounds(nr, nc):
                            diag_sum += self.grid[nr][nc]
        return diag_sum


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)