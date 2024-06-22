class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_count={}
        for i in nums:
            if i in freq_count:
                freq_count[i]+=1
            else:
                freq_count[i]=1
        max_count=0
        output=0
        for num,count in freq_count.items():
            if count>max_count:
                max_count,output=count,num
        return output 
            
        