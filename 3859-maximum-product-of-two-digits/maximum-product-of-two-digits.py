class Solution:
    def maxProduct(self, n: int) -> int:
        max=0
        n_list = [int(d) for d in str(n)]
        for i in range(len(n_list)):
            for j in range(i+1,len(n_list)):
                if n_list[i]*n_list[j]>max:
                    max = n_list[i]*n_list[j]
        return max
        