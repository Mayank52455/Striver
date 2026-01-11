class Solution:
    def second_largest_element(self, arr):
        if len(arr) < 2:
            return -1

        largest = second = float('-inf')

        for element in arr:
            if element > largest:
                second = largest
                largest = element
            elif largest > element > second:
                second = element

        return second if second != float('-inf') else -1
