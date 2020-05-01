class Solution(object):
    def isValid(self, s):
        temp = list()
        for brac in s:
            if brac in ('(', '{', '['):
                temp.append(brac)
            elif temp:
                if brac == ')' and temp[-1] == '(':
                    temp.pop()
                elif brac == '}' and temp[-1] == '{':
                    temp.pop()
                elif brac == ']' and temp[-1] == '[':
                    temp.pop()
            else:
                return False

        return len(temp) == 0


def main():
    a = Solution()
    s = '(]'
    print(a.isValid(s))


main()