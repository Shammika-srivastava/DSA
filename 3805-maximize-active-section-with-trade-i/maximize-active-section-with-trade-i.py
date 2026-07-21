class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ones = 0          # Count of already-active sections (number of '1's in the string)
        maxsum = 0        # Maximum combined length of two adjacent zero-runs
        prevrun = -1      # Length of the previous zero-run (-1 means none yet)
        i = 0

        while i < n:
            if s[i] == '1':
                # Each '1' represents an already-active section
                ones += 1
                i += 1
            else:
                # Measure the length of the current consecutive run of zeros
                curr = 0
                while i < n and s[i] == '0':
                    curr += 1
                    i += 1

                # If there was a previous zero-run, combine it with the current one
                # (they are separated by some ones, so one trade can merge them)
                if prevrun > 0:
                    maxsum = max(maxsum, prevrun + curr)

                # Update prevrun to the current zero-run length
                prevrun = curr

        # Final result = total ones + best possible merged zero-run length
        return ones + maxsum