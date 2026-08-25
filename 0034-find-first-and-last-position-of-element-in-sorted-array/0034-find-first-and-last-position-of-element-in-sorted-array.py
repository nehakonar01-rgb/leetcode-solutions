class Solution:
    def searchRange(self, nums, target):

        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    def findFirst(self, nums, target):

        left = 0
        right = len(nums) - 1

        answer = -1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                # We found target,
                # but there might be another target on the left
                answer = mid
                right = mid - 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return answer

    def findLast(self, nums, target):

        left = 0
        right = len(nums) - 1

        answer = -1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                # We found target,
                # but there might be another target on the right
                answer = mid
                left = mid + 1

            elif nums[mid] < target:

                left = mid + 1

            else:

                right = mid - 1

        return answer