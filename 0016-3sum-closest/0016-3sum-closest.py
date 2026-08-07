class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        n = len(nums)

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                if abs(target - current) < abs(target - closest):
                    closest = current

                if current < target:
                    left += 1

                elif current > target:
                    right -= 1

                else:
                    return current

        return closest