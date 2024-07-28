class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s1={}
        t1={}
        #key-character,value-index
        n=len(s)
        for i in range(n):
            s1[s[i]]=i
            t1[t[i]]=i
        sum=0
        for char,index in s1.items():
            sum=sum+abs(index-t1[char])
        return sum
