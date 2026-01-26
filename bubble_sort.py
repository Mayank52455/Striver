class solution:
  def bubble_sort(self, arr,n):
    for i in range (n):
      for j in range(n-1-i):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
