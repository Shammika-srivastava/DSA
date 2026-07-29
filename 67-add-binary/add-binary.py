class Solution:
    def addBinary(self, a: str, b: str) -> str:
    # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Add them
        total = num1 + num2
        
        # Convert back to binary string (remove '0b' prefix)
        return bin(total)[2:]
