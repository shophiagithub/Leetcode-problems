class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s.strip()
        s2=s1.split()
        length=len(s2[-1])
        return length
        