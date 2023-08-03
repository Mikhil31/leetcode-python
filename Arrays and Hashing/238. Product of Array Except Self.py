# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

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

        n =len(nums)

        left=[1]*n
        right= [1]*n

        for i in range(1,n):
            left[i] = left[i-1]* nums[i-1]

        #The code for i in range(n - 2, -1, -1) iterates over the numbers from n - 2 to -1 in reverse order. The range() function takes three arguments: the start value, the stop value, and the step size. In this case, the start value is n - 2, the stop value is -1, and the step size is -1.

        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        
        result=[]
        
        for i in range(n):
            result.append(left[i]*right[i])
        
        return result