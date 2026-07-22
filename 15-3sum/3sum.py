class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Sort the array to make duplicate handling easier
        nums.sort()
        result = []

        # Step 2: Iterate through each number as the fixed element (nums[k])
        for k in range(len(nums)):
            # Skip duplicate values for nums[k] to avoid repeated triplets
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            # Target is the negative of nums[k], because we want nums[i] + nums[j] + nums[k] = 0
            target = -nums[k]
            i = k + 1              # Left pointer
            j = len(nums) - 1      # Right pointer

            # Step 3: Use two-pointer technique to find pairs that sum to target
            while i < j:
                if nums[i] + nums[j] == target:
                    # Found a valid triplet
                    result.append([nums[k], nums[i], nums[j]])

                    # Skip duplicate values for nums[i]
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    # Skip duplicate values for nums[j]
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1

                    # Move both pointers inward after recording a triplet
                    i += 1
                    j -= 1

                elif nums[i] + nums[j] < target:
                    # If sum is too small, move left pointer to increase sum
                    i += 1
                else:
                    # If sum is too large, move right pointer to decrease sum
                    j -= 1

        # Step 4: Return all unique triplets
        return result
