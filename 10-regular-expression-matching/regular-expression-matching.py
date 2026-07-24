import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        raw = rf"p"
        if re.fullmatch(p,s):
            return True
        else:
            return False