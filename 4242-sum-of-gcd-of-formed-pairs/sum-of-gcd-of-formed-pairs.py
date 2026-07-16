class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b!=0:
                a,b = b,a%b
            return a

        max1 = nums[0]
        mx = []
        prefixGcd = []
        for i in range(len(nums)):
            if nums[i]>max1:
                max1 = nums[i]
            mx.append(max1)
            prefixGcd.append(gcd(nums[i],mx[i]))
        
        prefixGcd.sort()
        j = len(prefixGcd)-1
        sum1 =0
        for i in range(len(prefixGcd)):
            if i<j: # only run while i is strictly less than j
                sum1+=gcd(prefixGcd[i],prefixGcd[j])
                j-=1
            else: 
                break
        
        return sum1
