class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Get number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        
        # Total number of elements in the grid
        total = rows * cols

        # Step 1: Flatten the 2D grid into a 1D list
        # Example: [[1,2],[3,4]] → [1,2,3,4]
        flat = [grid[i][j] for i in range(rows) for j in range(cols)]

        # Step 2: Handle large k by modulo
        # Rotating by k > total is same as rotating by k % total
        k = k % total

        # Step 3: Perform the shift
        # Take last k elements and put them in front
        # Example: [1,2,3,4], k=2 → [3,4,1,2]
        flat = flat[-k:] + flat[:-k]

        # Step 4: Reshape the 1D list back into 2D grid
        result = []
        for i in range(rows):
            # Slice out each row of length 'cols'
            result.append(flat[i*cols:(i+1)*cols])

        # Step 5: Return the shifted grid
        return result
