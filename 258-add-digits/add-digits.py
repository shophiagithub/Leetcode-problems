class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        while(num>=10):
                digit=num%10+num//10
                num=digit
        return num