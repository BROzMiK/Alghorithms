"""
Given an array of characters arr, write a function that reverses the given array by
swapping equidistant elements from the start and the end.
"""


class Solution:
    def solution(self, arr: list[str]):
        if not arr:
            return []

        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
