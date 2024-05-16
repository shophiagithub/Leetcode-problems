class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==0:
            return 1
        curr,prev=1,1
        for i in range(2,n+1):
            temp=curr
            curr=prev+temp
            prev=temp
        return curr


        