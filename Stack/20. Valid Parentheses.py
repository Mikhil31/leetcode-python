# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brac = {'}': '{', ']': '[', ')': '('}

        for i in s:
            # check both key-value pairs to see if code is there or not in the first place
            # check if brac is a closing paren
            # if it is, it means that it only takes 2
            if i in brac:
                # now make sure that stack is empty (coz if stack is not empty it means there aer still come elements that are left and therefore invalid)
                # i will have values like (, {, [ etc in each iteration, we try to match if the topmost element in it is in stack
                if stack and stack[-1] == brac[i]:
                    # if they do match it meanas that we found an open-close pair
                    # and can now pop out the opening tag from the stack
                    stack.pop()
                else:
                    # if in top of elem on stack does not math with one brac it means that it's not valid
                    # cases like: (] or ) etc will fail
                    return False
            else:
                stack.append(i)

        return True if not stack else False
