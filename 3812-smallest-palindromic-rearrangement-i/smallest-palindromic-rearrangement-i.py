class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        odd_chars = [ch for ch, count in freq.items() if count % 2 == 1]

        # If more than one odd character, palindrome not possible
        if len(odd_chars) > 1:
            return ""

        # Build half of the palindrome
        half = []
        middle = odd_chars[0] if odd_chars else ""
        for ch in sorted(freq.keys()):
            half.extend([ch] * (freq[ch] // 2))

        half_str = "".join(half)
        return half_str + middle + half_str[::-1]

        