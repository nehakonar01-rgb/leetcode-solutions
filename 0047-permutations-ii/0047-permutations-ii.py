class Solution:
    def permuteUnique(self, nums):

        result = []
        current = []
        used = [False] * len(nums)

        # Sort so duplicate numbers are next to each other
        nums.sort()

        def backtrack():

            # Complete permutation
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):

                # Already used
                if used[i]:
                    continue

                # Skip duplicate numbers
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose
                current.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Undo
                current.pop()
                used[i] = False

        backtrack()

        return result