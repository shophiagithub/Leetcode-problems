class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        sum=1
        temp=num
        if temp>10**8 or temp<1:
            return False
       
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                t=num//i
                sum=sum+t+i
        if sum==temp:
            return True
        else:
            return False

        