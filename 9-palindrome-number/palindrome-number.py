class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        rev_num=0
        temp=x
        while x:
            digit=x%10
            rev_num=rev_num*10+digit
            x=x//10
        if(rev_num==temp):
            return True
        else:
            return False


        