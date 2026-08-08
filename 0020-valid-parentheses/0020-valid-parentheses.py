class Solution:
    def isValid(self, s):

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in '([{':
                stack.append(ch)

            # Closing bracket
            else:

                # No opening bracket available
                if not stack:
                    return False

                # Check if brackets match
                if stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        # Stack must be empty
        return len(stack) == 0