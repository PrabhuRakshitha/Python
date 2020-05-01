class Solution(object):
    def longestCommonPrefix(self, strs):
        str_prefix=''
        strs = sorted(strs)
        min_len = min(len(x) for x in strs)

        for i in range(min_len+1):
            temp=[x[0:i] for x in strs]
            if temp.count(temp[0]) == len(temp):
                str_prefix = temp[0]
        return str_prefix


def main():
    a = Solution()
    strs = ['flower','flow', 'tesr']
    print(a.longestCommonPrefix(strs))


main()



