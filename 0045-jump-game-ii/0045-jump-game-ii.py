class Solution:
    def jump(self, nums):
        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):

            # Find the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # We have reached the end of the current jump
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest

        return jumps