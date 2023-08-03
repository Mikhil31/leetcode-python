# https://leetcode.com/problems/koko-eating-bananas/

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #OBSERVATION

        """
        koko can eat k bananas in one hour (THE VAR WE NEED TO FIND)

        if koko needs to eat 4 bananas and piles are [3,6,7,11]
        in hour 1, koko eats 3 and exists for the rest of while (even thought it can eat one more) 

        we need to find min(k) such that koko can eat all the bananas before h hours

        len(piles) <= h, piles will always be less than or = to h, coz if it is greated koko wouldn't be able to finish the pile, i.e, if len(piles) == 4 and hours was 3, NO MATTER HOW FAST KOKO EATS IT WON'T FINISH PILE (coz it takes 1 hour per pile)


        we could use brute force, since every pile takes 1 hour, min is min k can is len(piles), max k can be maximum elem in pile, i.e, if koko can eat max no of piles in one hour, it can eat everything else in the same time too and since len(piles) <= h it should work in all cases  

        so, range(k) b/w len(piles) and max(piles)
        we can form an array and iterate though each value to find min of k where koko can finish bananas

        eg:[3,6,7,11] for this, arr will be [4(len),5,6...11(max)]

        """

        #from this take arr[i] as k and find how many hours it takes
        #for eg: [3,6,7,11] k = 4 to 11, try 4
        #piles[0]//4 (3//4) == 1 hours
        #piles[1]//4 (6//4) == 2 hours
        #piles[2]//4 (7//4) == 2 hours
        #piles[3]//4 (11//4)== 3 hours

                            #  8 hours
        # 8 hours == h so return 4 (arr[0]) if 8 hours != h, arr[i++]

        #BRUTE FORCE ALGO
        # add =0
     
        # for i in range(len(arr)):
        #     for j in range(len(piles)):
        #         div = int(piles[j]/arr[i])    
                
        #         print(piles[j], "//", arr[i], "= ", div)
        #         add += div

        #     if add == h:
        #         return arr[i]
        #     else:
        #         continue

        # return -1

        #declare arr that will have 1 to max(piles)
        #use binsearch on it 
        lo,hi=1,max(piles)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            count=0
            for i in piles:
                count+=i//mid
                if i%mid!=0:
                    count+=1
            if count>h:
                lo=mid+1
            else:
                hi = mid - 1
        return lo






