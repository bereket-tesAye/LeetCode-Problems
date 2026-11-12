class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            dig = 0
            while nums[i] > 0:
                nums[i] = nums[i]//10
                dig += 1
            if dig % 2 == 0:
                count += 1
        return count