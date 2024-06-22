class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        original_len=len(nums)
        new_list=[num for num in nums if num>=k]
        new_len=len(new_list)
        return original_len-new_len

        