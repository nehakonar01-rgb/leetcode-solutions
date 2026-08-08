class Solution:
    def generateParenthesis(self, n):

        result = []

        def backtrack(current, openCount, closeCount):

            # We have used all brackets
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add opening bracket
            if openCount < n:
                backtrack(
                    current + "(",
                    openCount + 1,
                    closeCount
                )

            # Add closing bracket
            if closeCount < openCount:
                backtrack(
                    current + ")",
                    openCount,
                    closeCount + 1
                )

        backtrack("", 0, 0)

        return result