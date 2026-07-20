class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        total = rows * cols

        # Flatten grid
        flat = [grid[i][j] for i in range(rows) for j in range(cols)]

        # Shift efficiently using modulo
        k = k % total
        flat = flat[-k:] + flat[:-k]

        # Reshape back to 2D
        result = []
        for i in range(rows):
            result.append(flat[i*cols:(i+1)*cols])
        return result