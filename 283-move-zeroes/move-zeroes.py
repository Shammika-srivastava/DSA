class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for k in range(len(nums)): 
            if nums[i]!=0:
                i+=1
        for j in range(i+1,len(nums)):
            if nums[j]!=0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                i+=1