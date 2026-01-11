class Solution:
    def rotate_array(self, arr, k):
        n = len(arr)
        k = k % n  # handle k > n

        def reverse(start: int, end: int):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the whole array
        reverse(0, n-1)
        # Step 2: Reverse first k elements
        reverse(0, k-1)
        # Step 3: Reverse remaining elements
        reverse(k, n-1)
