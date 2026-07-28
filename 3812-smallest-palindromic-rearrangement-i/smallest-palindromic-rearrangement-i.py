class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq={}
        for ch in s   :
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        left=[]
        mid="" 
        for ch in sorted(freq.keys()):
            left.append(ch*(freq[ch]//2))
            if freq[ch]%2==1:
                mid=ch
        left = "".join(left)
        right = left[::-1]

        return left + mid + right