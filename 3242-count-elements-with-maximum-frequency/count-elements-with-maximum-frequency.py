class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter 
        count=Counter(nums)
        max_count=max(count.values())
        return sum(count[k] for k in count if count[k]==max_count)