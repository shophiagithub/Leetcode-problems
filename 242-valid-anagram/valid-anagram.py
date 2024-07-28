class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1=list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        if(list1==list2):
            return True
        return False

        