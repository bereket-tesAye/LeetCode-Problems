class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        mx = 0
        sm = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                sm += accounts[i][j]
            mx = max(mx,sm)
            sm = 0
        return mx