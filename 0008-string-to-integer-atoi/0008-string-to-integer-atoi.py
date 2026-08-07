class Solution:
    def myAtoi(self, s):

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # If string contains only spaces
        if i == n:
            return 0

        # Check sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        result = 0

        # Read digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit

            i += 1

        result = result * sign

        # Clamp to 32-bit integer range
        if result > INT_MAX:
            return INT_MAX

        if result < INT_MIN:
            return INT_MIN

        return result        