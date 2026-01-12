class Solution:
    def max_cons_1(self, arr):
        current_count = 0
        max_count = 0

        for i in range(len(arr)):
            if arr[i] == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count
