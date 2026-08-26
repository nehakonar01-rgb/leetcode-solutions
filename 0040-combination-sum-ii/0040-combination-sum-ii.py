class Solution:
    def combinationSum2(self, candidates, target):

        result = []

        candidates.sort()

        def backtrack(start, target, current):

            # Target reached
            if target == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > target:
                    break

                # Choose current number
                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, target - candidates[i], current)

                # Backtrack
                current.pop()

        backtrack(0, target, [])

        return result