class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def combine(subset,v_str):
            new_sub=[]
            for i in range(len(subset)):
                for j in v_str:
                    new_sub.append(subset[i]+j)

            return new_sub

        output=[]
        digits=digits.strip()
        for dig in digits:
            if not output:
                output=['']

            output=combine(output,phone[dig])

        return output


def main():
    a=Solution()
    print(a.letterCombinations(''))

main()
