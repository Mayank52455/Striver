class solution:
  def twoSum(self, nums: list[int], target: int):
    s ={}
    for index, num in enumerate(nums):
      complement = target - num
      if complement in s:
        return [s[complement], index]

      s[num] = index
  retun []
