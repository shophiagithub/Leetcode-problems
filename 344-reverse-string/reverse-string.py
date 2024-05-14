class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #reversing string using for loop
        right=0
        temp=0
        left=len(s)-1
        while(right<left):
            temp=s[right]
            s[right]=s[left]
            s[left]=temp
            right+=1
            left-=1
        return s
        