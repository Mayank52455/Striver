class Solution:
    def missing_sum(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        difference_sum = expected_sum - actual_sum
        return difference_sum
