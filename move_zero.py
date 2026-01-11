class Solution:
    def movezero(self, nums):
        j = 0  # position for next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
