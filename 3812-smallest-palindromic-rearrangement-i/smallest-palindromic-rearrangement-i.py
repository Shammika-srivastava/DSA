class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Step 1: Count frequency of each character in the string
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1   # If character already exists, increase its count
            else:
                freq[ch] = 1    # Otherwise, initialize count as 1

        # Step 2: Prepare left half and middle character of palindrome
        left = []   # Will store half of the palindrome (left side)
        mid = ""    # Will store the middle character if any odd frequency exists

        # Step 3: Iterate characters in sorted order (lexicographically smallest palindrome)
        for ch in sorted(freq.keys()):
            # Add half of the occurrences of the character to the left side
            left.append(ch * (freq[ch] // 2))

            # If frequency is odd, one character will remain → candidate for middle
            if freq[ch] % 2 == 1:
                mid = ch   # Only one odd character can be in the middle

        # Step 4: Construct palindrome
        left = "".join(left)     # Convert list to string
        right = left[::-1]       # Mirror the left side to form the right side

        # Step 5: Return the smallest palindrome
        return left + mid + right
