class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = False
        max_len = 0
        n = len(s)
        substr =''
        if n == 1 or n==2:
            return s
        for i in range(n):
            counter = 1
            len_cnt = 1
            while i - counter >= 0 and i + counter < n:
                if s[i - counter] == s[i + counter]:
                    len_cnt = len_cnt + 2
                    if max_len < len_cnt:
                        max_len = len_cnt
                        substr = s[i - counter:len_cnt+1]
                else:
                    break
                counter = counter + 1

        for i in range(n):
            counter = 1
            len_cnt = 2
            while i - counter >= 0 and i + counter < n - 1:
                if s[i] != s[i + 1]:
                    break
                if s[i - counter] == s[i + 1 + counter]:
                    len_cnt = len_cnt + 2
                    if max_len < len_cnt:
                        substr = s[i - counter:len_cnt + 1]
                        max_len = len_cnt
                else:
                    break
                counter = counter + 1

        if max_len < len_cnt:
            max_len = len_cnt

        if substr == '':
            return s[0]
        else:
            return substr


if __name__ == "__main__":
    obj =Solution()
    s= 'afgf'
    out =obj.longestPalindrome(s)
    print(out)