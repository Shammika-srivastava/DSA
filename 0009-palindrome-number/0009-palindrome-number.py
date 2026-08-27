class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            num = [int(i) for i in str(x)]
            if num[::-1] == num:
                return True
        return False