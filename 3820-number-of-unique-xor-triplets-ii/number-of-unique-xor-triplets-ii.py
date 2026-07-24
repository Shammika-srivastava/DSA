from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        one, two, three = set(), set(), set()

        for x in nums:
            # add single element
            one.add(x)

            # update pairwise XORs
            for y in list(one):
                two.add(y ^ x)

            # update triple XORs
            for y in list(two):
                three.add(y ^ x)

        return len(three)
