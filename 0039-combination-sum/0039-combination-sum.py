class Solution:
    def combinationSum(self, candidates, target):

        result = []

        candidates.sort()

        def backtrack(start, target, current):

            if target == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                if candidates[i] > target:
                    break

                current.append(candidates[i])

                backtrack(
                    i,
                    target - candidates[i],
                    current
                )

                current.pop()

        backtrack(0, target, [])

        return result