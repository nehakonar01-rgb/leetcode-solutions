class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            width = right - left

            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1

            if area > maximum:
                maximum = area

        return maximum        