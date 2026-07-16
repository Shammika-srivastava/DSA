class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumEven=0
        count =n
        i=1
        while count!=0:
            if i%2==0:
                sumEven+=i
                count-=1
            i+=1
        j=1
        while n!=0:
            if j%2!=0:
                sumOdd+=i
                n-=1    
            j+=1    
            
        
        while sumEven!=0:
            sumOdd,sumEven = sumEven, sumOdd%sumEven
        
        return sumOdd