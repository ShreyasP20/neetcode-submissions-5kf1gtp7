class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue:
            row,col = queue.popleft()

            for dr,dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows)) and (c in range(cols)) and grid[r][c] == 2147483647:
                    grid[r][c] = grid[row][col] + 1
                    queue.append((r,c))