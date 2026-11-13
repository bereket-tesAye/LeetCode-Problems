class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums2 = []
        for i in range(n):
            nums2.append(nums[i])
            if n < len(nums):
                nums2.append(nums[n])
                n += 1
        return nums2
