class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def permute( v_str):
            output=[v_str,]
            for i in range(len(v_str)):
                for j in range(len(v_str)):
                    exp=list(v_str)
                    temp=exp[i]
                    exp[i]=exp[j]
                    exp[j]=temp
                    exp=''.join(exp)
                    if exp not in output and isvalid_exp(exp):
                        output.append(exp)

            return output

        def isvalid_exp(exp):
            temp=[]
            for i in exp:
                if i=='(':
                    temp.append(i)
                elif i ==')' and temp:
                    temp.pop()
                else:
                    return False

            return len(temp)==0

        v_str='('*n+')'*n
        output=permute(v_str)

        return output


def main():
    a=Solution()
    print(a.generateParenthesis(4))


main()
