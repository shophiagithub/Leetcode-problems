class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum=0
        for i in s:
            sum=sum+abs(s.index(i)-t.index(i))
        return sum