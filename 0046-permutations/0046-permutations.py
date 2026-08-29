class Solution:
    def permute(self, nums):

        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            # If current permutation contains all numbers
            if len(current) == len(nums):
                result.append(current[:])
                return

            # Try every number
            for i in range(len(nums)):

                # Skip if already used
                if used[i]:
                    continue

                # Choose
                current.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Undo choice
                current.pop()
                used[i] = False

        backtrack()

        return result