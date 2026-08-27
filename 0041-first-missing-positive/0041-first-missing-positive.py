class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Put every number x at index x - 1
        i = 0

        while i < n:
            correct_index = nums[i] - 1

            if (nums[i] > 0 and
                nums[i] <= n and
                nums[i] != nums[correct_index]):

                nums[i], nums[correct_index] = nums[correct_index], nums[i]

            else:
                i += 1

        # Find the first position where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1