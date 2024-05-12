class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum=0
        temp=x
        while(x>0):
            digit=x%10
            sum=sum+digit
            x=x//10
        if(temp%sum==0):
            return sum
        else:
            return -1

        