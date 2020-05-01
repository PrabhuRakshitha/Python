class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=''
        for i in range(len(s)):
            for j in range( 1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(output)< len(s[i:j]):
                       output=s[i:j]

        return output


def main():
    a=Solution()
    print(a.longestPalindrome('b'))


main()