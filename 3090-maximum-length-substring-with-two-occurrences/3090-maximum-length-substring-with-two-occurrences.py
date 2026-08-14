class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Add current character
            seen[s[right]] = seen.get(s[right], 0) + 1

            # Shrink window if invalid
            while seen[s[right]] > 2:
                seen[s[left]] -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
