#  waht if string is null

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        start =0
        pos_dict = dict()
        substr = ''
        for i in range(len(s)):
            if s[i] in pos_dict and pos_dict[s[i]] >= start:
                if max_len < i-start:
                    max_len = i-start
                start = pos_dict[s[i]]+1
                pos_dict[s[i]] = i
            else:
                pos_dict[s[i]] =i

        if max_len < i-start+1:
            max_len = i-start+1

        return max_len

if __name__ == "__main__":
    obj = Solution()
    x ='pwwkew'
    print(obj.lengthOfLongestSubstring(x))










