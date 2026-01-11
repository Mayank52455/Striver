class Solution:
  def sorted_and_rotared(self, arr):
  n = len(arr)
  if n == 1:
    return True
  count = 0
  for i in range (1, n):
    if arr[i] > arr[(1+i) %n]:
      count+=1
  return count<=1
