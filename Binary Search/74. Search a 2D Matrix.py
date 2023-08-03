# https://leetcode.com/problems/search-a-2d-matrix/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col = 0

        for i in range(len(matrix)):
            if target < matrix[i][-1]:
                col = i
                break
            elif target == matrix[i][-1]:
                return True

        # do bin search in col
        if col >= 0:
            arr = matrix[col]
            start = 0
            end = len(arr)-1

            while start <= end:
                mid = start + (end-start)//2

                if arr[mid] == target:
                    return True
                    break
                elif arr[mid] < target:
                    start = mid + 1
                elif arr[mid] > target:
                    end = mid - 1

            return False
