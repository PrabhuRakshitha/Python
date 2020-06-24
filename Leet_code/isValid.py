class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for braces in s:
            if braces in ('(', '{','['):
                stack.append(braces)
            elif stack and braces in (')','}',']'):
                if stack[-1] =='(' and braces ==')':
                    stack.pop()
                elif stack[-1] =='[' and braces ==']':
                    stack.pop()
                elif stack[-1] =='{' and braces =='}':
                    stack.pop()
            else:
                return False

        return True

if __name__ =='__main__':
    obj = Solution()
    out =obj.isValid('()')
    print(out)
