class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # First n odd numbers: 1, 3, 5, ..., (2n-1)
        sumOdd = sum(2*i - 1 for i in range(1, n+1))
        # First n even numbers: 2, 4, 6, ..., (2n)
        sumEven = sum(2*i for i in range(1, n+1))

        # Euclidean algorithm for GCD
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return gcd(sumOdd, sumEven)
