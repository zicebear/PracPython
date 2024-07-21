class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            # 因为经过了排序，所以：
            # 如果第一个数大于零，那么之后的数也肯定都大于零，三数之和一定大于零
            # 如果后两个数的和都小于零，意味着最大的两个数之和小于零，那么三数之和一定小于零
            if nums[i] > 0 or nums[-1] + nums[-2] < 0:
                break
            # 下面这句要注意满足 i > 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # 上面三个数相加等于零，如果只移动 j 或 k 一个指针的话，那三数之和肯定就不是零了
                    # 所以 j 和 k 都要移动
                    j += 1
                    k -= 1
                    # 而且如果 j 或 k 和之前相等的话，也要和 i 一样跳过，避免重复
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res
    
nums = [0,-4,-1,-4,-2,-3,2]
mysolution = Solution()
print(mysolution.threeSum(nums))