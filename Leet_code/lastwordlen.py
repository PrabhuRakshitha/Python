class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip(' ')
        v_len=s.rfind(' ')
        return len(s[v_len+1:])

def main():
    a=Solution()
    print(a.lengthOfLastWord("hello am herevvv"))


main()