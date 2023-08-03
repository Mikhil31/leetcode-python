# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:


# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    #     n = len(nums)
    #     left_product = [1] * n # initialize left_product array with 1
    #     right_product = [1] * n # initialize right_product array with 1
    # # calculate the product of elements to the left of each element
    #     for i in range(1, n):
    #         left_product[i] = left_product[i - 1] * nums[i - 1]

    # # calculate the product of elements to the right of each element
    #     for i in range(n - 2, -1, -1):
    #         right_product[i] = right_product[i + 1] * nums[i + 1]

    # # calculate the product of all elements except nums[i]
    #     result = [left_product[i] * right_product[i] for i in range(n)]

        n = len(nums)

        left = [1]*n
        right = [1]*n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # The code for i in range(n - 2, -1, -1) iterates over the numbers from n - 2 to -1 in reverse order. The range() function takes three arguments: the start value, the stop value, and the step size. In this case, the start value is n - 2, the stop value is -1, and the step size is -1.

        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]

        result = []

        for i in range(n):
            result.append(left[i]*right[i])

        return result
