# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}

        for i in range(len(strs)):
            sortedWord = " ".join(sorted(strs[i]))
            if sortedWord not in dict:
                dict[sortedWord] = [strs[i]]
            else:
                # sort it first, if value is found, jsut append to that array in dict, we've defined it as in array in line 11
                dict[sortedWord].append(strs[i])

        # values is the 2nd one in the dict
        # dict: {u'a b t': [u'bat'], u'a e t': [u'eat', u'tea', u'ate'],
        # u'an t': [u'tan', u'nat']}

        return dict.values()
