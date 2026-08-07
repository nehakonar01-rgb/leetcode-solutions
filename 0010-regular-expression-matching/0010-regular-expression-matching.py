class Solution:
    def isMatch(self, s, p):

        memo = {}

        def dp(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            firstMatch = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j + 1] == '*':

                ans = dp(i, j + 2) or (
                    firstMatch and dp(i + 1, j)
                )

            else:

                ans = firstMatch and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)