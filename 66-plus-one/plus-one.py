class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]==9: #assigns 0 instead of 9
                digits[i]=0
            else:
                digits[i]+=1 
                return digits
        return [1]+digits #handlse the case when all digits are 9

        