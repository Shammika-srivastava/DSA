class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                temperatures[idx] = i - idx
            stack.append(i)
        
        while stack:
            temperatures[stack.pop()]=0
        
        return temperatures