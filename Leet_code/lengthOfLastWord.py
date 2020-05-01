class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip()
        count=0
        for i in range(len(s)-1, 0):
            if s[i]==' ':
                return count
            else:
                count=count+1

        return count

def main():
    a=Solution()
    print(a.lengthOfLastWord("test here"))

main()