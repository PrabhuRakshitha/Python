class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        for i in range(n):
            if i==0:
                nums="1"
            else:
                temp=nums
                say=nums[0]
                nums=''
                count=0
                for dig in temp:
                    if say==dig:
                        count=count+1
                    else:
                        nums=nums+str(count)+str(say)
                        say=dig
                        count=1
                nums =nums + str(count) + str(say)

        return nums


def main():
    a = Solution()
    print(a.countAndSay(4))


main()
