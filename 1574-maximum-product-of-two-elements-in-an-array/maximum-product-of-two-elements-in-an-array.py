class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        max =0
        i=0
        for j in range(1,len(nums)):
            if (nums[i]-1) * (nums[j]-1)>max:
                max = (nums[i]-1) * (nums[j]-1)
            i+=1
        return max 
       
    