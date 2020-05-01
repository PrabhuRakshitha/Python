class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output=''
        temp=[]
        for v_char in s:
            print(output)
            if v_char in output:
                temp.append(len(output))
                output=output[output.find(v_char)+1:] +v_char
            else:
                output=output+v_char

        temp.append(len(output))
        return max(temp)



def main():
    a=Solution()
    print(a.lengthOfLongestSubstring("dvdf"))


main()

