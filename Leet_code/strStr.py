class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen=len(needle)
        if not haystack and not needle:
            return 0
        for i in range(len(haystack)-nlen):
            if haystack[i:i+nlen] == needle:
                return i

        return -1

def main():
    a=Solution()
    print(a.strStr('',''))


main()