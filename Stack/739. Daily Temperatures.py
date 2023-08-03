# https://leetcode.com/problems/daily-temperatures/

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        st = []

        for i in range(0, n):
            while (len(st)>0) and temperatures[i]> temperatures[st[len(st)-1]]:
              index = st[len(st)-1]
              st.pop()
              ans[index] = i-index
            st.append(i)
      
        return list(ans)   

    # Temperature: 73, Index: 0
# The stack is empty, so the current temperature index is added to the stack.
# Stack: [0]
# Temperature: 74, Index: 1
# The current temperature (74) is greater than the temperature at index 0 (73).
# We pop the top of the stack and set ans[0] to the difference between the current index (1) and the popped index (0): ans[0] = 1.
# Stack: [] (Empty stack after popping)     
                
        
