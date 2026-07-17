class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Xor = 0
        for i in range(1,len(nums)+1):
            Xor ^= i
        for i in nums:
            Xor^=i
        return Xor