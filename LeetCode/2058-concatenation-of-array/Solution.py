class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length_of_arr = len(nums)
        ans = []
        for i in range(length_of_arr):
            nums.append(nums[i])
            
        return nums