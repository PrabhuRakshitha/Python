# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        start = -1
        while i < len(haystack):
            if j == len(needle):
                break
            if haystack[i] == needle[j]:
                if j == 0:
                    start = i
                i = i + 1
                j = j + 1
            elif j > 0:
                j = 0
                i = start + 1
                start = -1
            else:
                i = i + 1

        if j != len(needle):
            return  -1
        else: return start




if __name__ == "__main__":
    obj = Solution()
    out = obj.strStr('aa', 'aaa')
    print(out)


