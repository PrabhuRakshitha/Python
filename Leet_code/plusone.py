class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rem=1
        for i in range((len(digits)-1),-1,-1):
            temp=(digits[i]+rem)%10
            rem=(digits[i]+rem)//10
            digits[i]=temp
            print (rem)

        if rem >0:
            digits.insert(0,rem)

        return digits

def main():
    a=Solution()
    print(a.plusOne([9]))

main()
