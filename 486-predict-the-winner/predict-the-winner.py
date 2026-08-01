from functools import lru_cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def diff(i, j):
            if i == j:
                return nums[i]
            # Choose left or right
            left = nums[i] - diff(i + 1, j)
            right = nums[j] - diff(i, j - 1)
            return max(left, right)
        return diff(0, len(nums) - 1) >= 0
