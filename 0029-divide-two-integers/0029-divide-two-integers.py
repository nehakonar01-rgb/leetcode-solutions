class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            value = divisor
            multiple = 1

            # Double the divisor using bit shifting
            while value + value <= dividend:
                value = value << 1
                multiple = multiple << 1

            # Subtract the largest possible multiple
            dividend = dividend - value
            quotient = quotient + multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp to 32-bit range
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient