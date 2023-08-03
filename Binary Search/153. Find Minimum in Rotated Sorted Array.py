# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # simple sol that takes nlog n time
        # nums = sorted(nums)
        # return nums[0]

        # find mid in arr, take the mid -1 elem nad mid+1 elem, which ever is lesser that will be the side to search on

        start = 0
        end = len(nums)-1
        res = nums[0]

        while start <= end:

            # check if start elem >= mid, if so it means that portion of the array won't hvae min coz it's already sorted arr
            # if nums[start] < nums[end]:
            #     res = min(res, nums[start])
            #     break
            # so we search in right portion of the arr
            mid = start + (end-start) // 2
            res = min(res, nums[start])
            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid - 1

        return res
