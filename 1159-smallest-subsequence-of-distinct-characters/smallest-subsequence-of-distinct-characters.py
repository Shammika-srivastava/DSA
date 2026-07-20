class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []  # Monotonic stack to build the subsequence
        seen = set()  # Tracks which characters are already in the stack (avoid duplicates)

        # Map each character to its last occurrence index in the string
        # Example: for "cbacdcbc" → {'c':7, 'b':6, 'a':2, 'd':5}
        last_index = {ch: i for i, ch in enumerate(s)}  
    
        # Iterate through each character with its index
        for i, ch in enumerate(s):
            # If character already in stack, skip it (we only want unique characters)
            if ch in seen:
                continue

            # While stack is not empty AND current char is smaller than stack top
            # AND the stack top appears later again in the string:
            # → pop stack top to get lexicographically smaller result
            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                seen.remove(stack.pop())

            # Add current character to stack
            stack.append(ch)
            seen.add(ch)

        # Convert list of characters into final string
        return "".join(stack)
