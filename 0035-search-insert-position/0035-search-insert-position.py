class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target is on the right
            elif nums[mid] < target:
                left = mid + 1

            # Target is on the left
            else:
                right = mid - 1

        # Target not found
        # left is the correct insertion position
        return left