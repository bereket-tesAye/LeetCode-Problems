class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        temp = x
        if x < 0:
            return False

        while x > 0:
            dig = x % 10 
            rev = rev * 10 + dig
            x = x // 10
             
        return (rev == temp)


