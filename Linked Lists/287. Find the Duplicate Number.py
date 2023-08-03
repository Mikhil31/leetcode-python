# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3


# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.


# BOTH SOLUTIONS ARE NOT FEASIBLE
# sorting alters num which violates the condition
# hash Maps take O(n) space

# USE LINKED LIST

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # SOLUTION 2 (invalid)

        # hashMap={}

        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 0

        # for i in range(len(nums)):
        #     hashMap[nums[i]] += 1
        #     if hashMap[nums[i]] > 1:
        #         return nums[i]
        #         break

        # SOLUTION 3 (Invalid)

        # SOLUTION FEASIBLE IF NUMS CAN BE SORTED BUT ACC TO QUES,CAN'T DO THAT
        # sort the arr first
        # nums = sorted(nums)
        # num=0
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         num= nums[i]
        #         return num
        #         break

        return -1
