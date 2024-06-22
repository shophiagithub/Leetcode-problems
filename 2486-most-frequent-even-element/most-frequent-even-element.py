class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_count={}
        for i in nums:
            #extracting only the even numbers 
            if i%2==0:
                freq_count[i]=1 if i not in freq_count else freq_count[i]+1
        max_count=0
        output=-1
        for num,count in freq_count.items():
            if count>max_count:
                max_count,output=count,num
            elif count==max_count:
                output=min(num,output)
        return output 


                
        