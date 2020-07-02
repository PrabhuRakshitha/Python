class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alpha =  {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o']
                   , '7':['p','q','r','s'], '8':['t','u','v'],'9':['w','x','y','z']}
        out =[]

        def backtrack(pattern, nextdig):
            if len(nextdig) ==0:
                out.append(pattern)
            else:
                dig = nextdig[0]
                for i in alpha[dig]:
                    backtrack(pattern+i , nextdig[1:])

        if digits:
            backtrack('',digits)
        return out



if __name__ =="__main__":
    obj = Solution()
    out = obj.letterCombinations('23')

    print(out)
