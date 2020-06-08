class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        orig =x
        rev =0
        while orig >0:
            rev = rev * 10 + ( orig %10)
            orig = orig //10

        if x == rev :
            return True
        else:
            return False
