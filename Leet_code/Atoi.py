class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        output=0
        sign=1

        if str[0] == '-':
            sign=-1
            str=str[1:]
        elif str[0] == '+':
            sign=1
            str = str[1:]

        for v_char in str:
            if not v_char.isnumeric():
                break
            else:
                output=output*10+int(v_char)
        output=output*sign

        if output > (2**31)-1:
            return (2**31)-1
        elif output < -1* (2**31):
            return -1*(2**31)

        return output


def main():
    a=Solution()
    print(a.myAtoi(''))

main()