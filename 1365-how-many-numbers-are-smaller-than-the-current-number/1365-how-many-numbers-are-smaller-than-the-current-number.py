class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
    
        # Dictionary: number → count of smaller elements
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:   # only store first occurrence
                rank[num] = i
        
        # Build result using the dictionary
        return [rank[num] for num in nums]