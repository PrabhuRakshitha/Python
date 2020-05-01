class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mult=1
        output=''
        for dig in reversed(str(num)):
            temp=int(dig)*mult
            if temp >=1000:
                output='M'*(temp//mult) +output

            elif temp==400:
                output='CD'+output
            elif temp==900:
                output='CM'+output
            elif temp >=500:
                output='D'+'C'*((temp-50)//mult) +output
            elif temp<400 and temp >=100:
                output='C'*(temp//mult) +output

            elif temp==40:
                output='XL'+output
            elif temp==90:
                output='XC'+output
            elif temp >=50:
                output ='L'+'X'*((temp-50)//mult) +output
            elif temp <40 and temp >=10:
                output='X'*(temp//mult) +output

            elif temp==9:
                output='IX'+output
            elif temp==4:
                output='IV'+output
            elif temp < 4 and temp >=1:
                output= 'I'*(temp//mult)+output
            elif temp >=5:
                output='V'+ 'I'*((temp-5)//mult)+output

            mult=mult*10
        return output


def main():
    a=Solution()
    print(a.intToRoman(1995))


main()