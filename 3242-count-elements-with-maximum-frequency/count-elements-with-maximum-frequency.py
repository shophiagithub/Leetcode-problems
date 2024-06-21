class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_count={}
        for num in nums:
            if num in freq_count:
                freq_count[num]+=1
            else:
                freq_count[num]=1
        
        max_freq=0
        for freq in freq_count.values():
            if freq>max_freq:
                max_freq=freq

        total_occurence=0 #to count the total occurence of the maximum frequency 
        for num,freq in freq_count.items():
            if freq==max_freq:
                total_occurence+=freq
        return total_occurence 

        