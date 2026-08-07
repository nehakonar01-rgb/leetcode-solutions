class Solution:
    def longestPalindrome(self, s):

        if len(s) < 2:
            return s

        start = 0
        maxLength = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            # Odd length palindrome
            left1, right1 = expand(i, i)

            if right1 - left1 + 1 > maxLength:
                start = left1
                maxLength = right1 - left1 + 1

            # Even length palindrome
            left2, right2 = expand(i, i + 1)

            if right2 - left2 + 1 > maxLength:
                start = left2
                maxLength = right2 - left2 + 1

        return s[start:start + maxLength]