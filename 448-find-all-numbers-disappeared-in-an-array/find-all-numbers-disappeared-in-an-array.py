class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        n = len(nums)
        full_set = set(range(1,n+1))
        return list(full_set - nums_set)
           
