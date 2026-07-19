class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        last_index = {ch: i for i, ch in enumerate(s)}  # last occurrence
    
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)