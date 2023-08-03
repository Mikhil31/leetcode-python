# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # solve using 2 pointers method
        # point one to start of the LL and the other to end of the LL

        # curr to head means that that LL is pointing to the last elem
        prev, curr = None, head

        # need to iteratively loop through till curr is not null
        while curr:
            # [5,4,3,2,1] (before and after 5 and 1 there's NULL values)for this arr, intially prev will point Null value that is before 5 and curr point to 1(in the LL)

            # during 1st ite, swap NULL (that is prev) to curr and prev should will point to next elem

            # swap 5 and 1 in iteration 1 and so on
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
