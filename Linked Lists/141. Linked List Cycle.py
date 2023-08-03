# https://leetcode.com/problems/linked-list-cycle/ 

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime
# 30ms
# Beats 96.91% of users with Python

# Memory
# 20.56mb
# Beats 23.78% of users with Python

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # create fast and slow pointer
        # fast += 2 (traverse 2 nodes once)
        # slow += 1

        # as we traverse through Linked List fast and slow have to meet at some point
        # coz for every +1 of slow fast is +2

        # (so if dist b/w slow and fast is 5, then next dist= 6+(1-2) 1 by slow and 2 by fast)

        # intialiaze slow and fast to head and inc in loop
        slow = head
        fast = head

        # run till fast reaches None or end of node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # keep iterating till fast catches upto slow
            if slow == fast:
                return True

        return False
