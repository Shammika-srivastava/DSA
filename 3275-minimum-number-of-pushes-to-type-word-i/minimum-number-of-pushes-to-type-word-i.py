class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        result = 0
        if len(word)<=8:
            return len(word)
        for i in range(1,(len(word)//8)+1):
            result += i*8
            count =i
        return result+(count+1)*(len(word)%8) 
        
    
    
    
    
    
    
 
# lass Solution:
#     def minimumPushes(self, word: str) -> int:
#         if  len(word)>8 and len(word)<=16
#              rturn 8 + 2 * len()ord[8:]))
#         return len(word)
#         f leen(word)>16 and ln(word)<=24:
#             return 8+(2len(word[8)1)*len(word[16:])])) 