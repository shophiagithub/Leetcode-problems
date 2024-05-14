class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #reversing string using for loop
        new_str=""
        for i in range(len(s)):
            new_str=s[i]+new_str
        s[:]=list(new_str)
        return s
        