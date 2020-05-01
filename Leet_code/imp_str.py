class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+nlen] == needle:
                return i

        return -1

def main():
    a=Solution()
    print(a.strStr('hello','x'))


main()