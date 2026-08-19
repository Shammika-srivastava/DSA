class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        X= nums[0:n]
        Y= nums[n:]
        result=[]
        for i in range(n):
            result.append(X[i])
            result.append(Y[i])
        return result

        # result = []
        # for i in range(n):
        #     result.append(nums[i])      # first half
        #     result.append(nums[i+n])    # second half
        # return result