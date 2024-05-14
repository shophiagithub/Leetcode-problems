class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        while(True):
            if num<10:
                return num
            digit=num%10+num//10
            num=digit