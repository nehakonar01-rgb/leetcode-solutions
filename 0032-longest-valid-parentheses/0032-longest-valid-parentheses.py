class Solution:
    def longestValidParentheses(self, s):

        stack = [-1]
        maxLength = 0

        for i in range(len(s)):

            if s[i] == '(':

                # Store index of opening bracket
                stack.append(i)

            else:

                # Remove the matching opening bracket
                stack.pop()

                if not stack:
                    # Current ')' cannot be matched
                    stack.append(i)

                else:
                    # Length of valid substring
                    length = i - stack[-1]

                    if length > maxLength:
                        maxLength = length

        return maxLength