class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        solution = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    solution += 4
                    if i < m - 1 and grid[i+1][j] == 1:
                        solution -= 2
                    
                    if j < n - 1 and grid[i][j+1] == 1:
                        solution -= 2
        

        return solution