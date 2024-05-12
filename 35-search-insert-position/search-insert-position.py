class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                nums[i]=target
                return i
            elif i<len(nums)-1 and target>nums[i] and target<nums[i+1]:
                nums.insert(i+1,target)
                return i+1
            
        return len(nums)

        

        