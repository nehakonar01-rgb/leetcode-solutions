class Solution:
    def canJump(self, nums):

        farthest = 0

        for i in range(len(nums)):

            # If current index cannot be reached
            if i > farthest:
                return False

            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # Already reached the last index
            if farthest >= len(nums) - 1:
                return True

        return False