class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        for i in nums:
            if i!=val:
                nums[count]=i
                count+=1
        return count
    
        #i = 0
        #for x in nums:
            #if x != val:
                #nums[i] = x
                #i += 1
        #return i