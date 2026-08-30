class Solution:
    def myPow(self, x, n):

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:

            # If n is odd
            if n % 2 == 1:
                result = result * x

            # Square x
            x = x * x

            # Divide n by 2
            n = n // 2

        return result