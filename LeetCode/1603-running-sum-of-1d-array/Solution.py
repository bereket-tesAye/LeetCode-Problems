
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sm = 0
        runningSum = []
        length_of_arr = len(nums)
        for i in range(length_of_arr):
            sm+=nums[i]
            runningSum.append(sm)

        return runningSum