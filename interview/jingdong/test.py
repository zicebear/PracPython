class Solution:
    def zeroList(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
                right = right -1
            elif nums[left] != 0:
                left = left + 1
        return nums

nums = [0, 1, 2, 3, 0, 2]
test = Solution()
print(test.zeroList(nums))