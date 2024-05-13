class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniquenum=0
        for i in nums:
            uniquenum=uniquenum^i
        return uniquenum

        
        