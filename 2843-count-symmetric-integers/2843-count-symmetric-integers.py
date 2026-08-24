class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2 == 0:  # only even digit numbers
                mid = len(s) // 2
                sum1 = sum(map(int, s[:mid]))
                sum2 = sum(map(int, s[mid:]))
                if sum1 == sum2:
                    num += 1
        return num
        num = 0
        # for i in range(low, high+1):
        #     # count digits
        #     digits = []
        #     n = i
        #     while n > 0:
        #         digits.append(n % 10)
        #         n //= 10
        #     digits.reverse()  # now in correct order

        #     if len(digits) % 2 == 0:  # only even digit numbers
        #         mid = len(digits) // 2
        #         sum1 = sum(digits[:mid])
        #         sum2 = sum(digits[mid:])
        #         if sum1 == sum2:
        #             num += 1
        # return num
