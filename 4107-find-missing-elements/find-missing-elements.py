class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = 0
        # XOR all values in the range
        for i in range(min(nums), max(nums)+1):
            if i < len(nums):
                result ^= i ^ nums[i]
            else:
                result ^= i
        # Convert XOR result into a list of missing numbers
        missing = []
        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                missing.append(i)
        return missing
