# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        # the dic will have count of all the numbers (1:3, 2:2, 3:1)
        # sort this dic first in ascending order

        # the output will have a tuple
        # key pair will have tuple (1, 3), (2, 2), (3, 1)
        sortedCount = sorted(count.items(), key=lambda x: x[1], reverse=1)

        # gives tuple as output
        # access tuple in range of k
        newList = []
        for i in range(k):
            if i < len(sortedCount):
                newList.append(sortedCount[i][0])
            else:
                break

        return newList
