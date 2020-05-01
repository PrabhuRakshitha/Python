class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output=''
        temp1=list(a)
        temp2=list(b)
        rem=0
        while temp1 or temp2:
            if temp1 and temp2:
                dig = int(temp1.pop())+int(temp2.pop()) + rem
                rem = dig//2
                dig = dig % 2
                output = str(dig) + output
            elif temp1:
                dig=int(temp1.pop())+rem
                rem = dig //2
                dig = dig % 2
                output = str(dig) + output
            else:
                dig = int(temp2.pop()) + rem
                rem = dig // 2
                dig = dig % 2
                output = str(dig) + output

        if rem > 0:
            output=str(rem)+output

        return output



def main():
    a=Solution()
    print(a.addBinary('0','0'))


main()
