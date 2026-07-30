class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        elif len(word)<=16:
            return 8 + (2 * len(word[8:]))
        elif len(word)<=24:
            return 8+(2*len(word[8:16]))+(3*len(word[16:]))
        else:
            return 8+(2*len(word[8:16]))+(3*len(word[16:24]))+(4*len(word[24:]))