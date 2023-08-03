# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # convert first LL to number and reverse it
        curr = l1
        num1 = ""
        while curr:
            num1 += str(curr.val)
            curr = curr.next

        num1 = num1[::-1]
        num1 = int(num1)

        # convert 2nd LL (l2) to num and reverse it
        curr = l2
        num2 = ""
        while curr:
            num2 += str(curr.val)
            curr = curr.next

        num2 = num2[::-1]
        num2 = int(num2)

        res = num1+num2
        res = str(res)
        res = res[::-1]

        link = list(res)

        for i in range(len(link)):
            link[i] = int(link[i])

        linkedList = ListNode()
        curr = linkedList
        for digit in link:
            node = ListNode(digit)
            curr.next = node
            curr = curr.next

        return linkedList.next
