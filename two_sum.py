class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for index, num in enumerate (nums):
            complement = target - num
            if complement in s:
                return [s[complement], index ]
            

            s[num] = index
        return[]
