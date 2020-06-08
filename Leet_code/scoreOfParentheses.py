class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack =[]
        for sub in S:
            num =0
            # print(stack)
            if sub =='(':
                stack.append(sub)
            elif sub ==')':
                while stack[-1] !='(':
                    num = num + stack.pop()
                stack.pop()
                if num > 0:
                    stack.append(num *2)
                else:
                    stack.append(1)
        out =0
        while stack:
            out += stack.pop()
        return out

if __name__ =="__main__":
    obj = Solution()
    S ='(()(()))()'
    out = obj.scoreOfParentheses(S)
    print(out)


