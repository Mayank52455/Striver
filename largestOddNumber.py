class Solution:
  def largest_odd_number(self, num: str):
    for i in range(len(num)-1, -1, -1):
      if int(num[i]) %2 != 0:
        return [ : i+1]
    return ""
