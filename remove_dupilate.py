class Solution:
  def remove_dupilate (self, arr):
    if len(arr) == 1:
      return 1
    k = 1
    n = len(arr)
    for i in range (1, n):
      if arr[i] != arr[k-1]:
        arr[k] = arr[i]
        k+=1
    return k
