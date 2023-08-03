# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # can be considered a 2 pointer problem, take 2 pointers L and R

        # intially the left is in first elem and right is n nodes away from L
        # in [1,2,3,4,5,6] if n=2, we need traverse from 6 and delete 2nd elem(which is node 4),in this case L=1 and R= 3 (2(n) nodes away)

        # Traverse till R reaches null

        # so R will be 3 -> 4 -> 5 -> 6 -> None (4 nodes) and L pointer will be at 1 -> 2 -> 3 -> 4 (R will now point to our elem)

        # to delete a node we need to take the node's prev link and attack that to the node's next (3 is to be linked to 5 and remove 4)

        # to do this we need to R to point to 4, which means we need another dummy node to start from, so that we end up at the (n-1)th node

        # initialize dummy node
        # to create one, we can just enter it's val and it's "head" or define where it should point to
        # val : 0, points to head (so will attach to head(to node 1))
        dummy = ListNode(0, head)

        # define left pointer
        left = dummy

        # define right (n nodes away from L)
        # can't do head+n, coz it's a nested DICT, so use loop to do
        # right.next (point to next elem)

        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        # keep shifting till right = None
        while right:
            left = left.next
            right = right.next

        # now left will point to n-1th node
        # delete node
        # left.next (which is node taht we want) will point to next.next
        # so from 3 it will go to 5 in eg (and miss 4)

        left.next = left.next.next

        # return the LL(dummy.next and not head, coz that's not waht we delted)
        return dummy.next
