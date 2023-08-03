# https://leetcode.com/problems/merge-two-sorted-lists/

# 21. Merge Two Sorted Lists
# Easy
# 19.4K
# 1.8K
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create a dummy LL and from that
        dup = ListNode()
        linkList = dup

        # inside the linked list, check if values are equal
        # if val in list 1 is greater, append that to linkList
        # vice verso if l2 >l1

        while list1 and list2:
            if list1.val < list2.val:
                linkList.next = list1
                list1 = list1.next
            else:
                # if val at l2 is not greater it can only mean that l2 is greater or l2 is greater, append l2 now
                linkList.next = list2
                list2 = list2.next

            # increment linkList var in either of the cases
            linkList = linkList.next

            # either list1/list2 can be empty or one of the list may have finished traversing

        # check if l1/l2 are empty

        linkList.next = list1 or list2
        return dup.next
