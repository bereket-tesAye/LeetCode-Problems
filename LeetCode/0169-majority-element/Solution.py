class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        for i in cnt:
            if cnt[i] > len(nums)/2:
                return i
        