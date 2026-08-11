class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i = 1  # start from 1
        for num in target:
            while i < num:
                result.append("Push")
                result.append("Pop")
                i += 1
            result.append("Push")
            i += 1
        return result