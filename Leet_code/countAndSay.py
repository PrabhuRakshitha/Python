# The count-and-say sequence is the sequence of integers with the first five terms as following:

class Solution(object):
    def countAndSay1(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        out ="1"

        for i in range(n-1):
            temp =''
            prev =''
            count= 0
            for j in range(len(out)):
                if j ==0:
                    prev = out[j]
                    count = 1
                elif prev == out[j]:
                    count = count + 1
                    prev = out[j]
                else:
                    temp = temp +str(count) + prev
                    prev = out[j]
                    count = 1

            out = temp +str(count) + prev
        return out

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        out =''
        for i in range(len(prev)):
            if i ==0:
                temp= prev[i]
                count =1
            elif temp == prev[i]:
                count =count+1
            else:
                out = out + str(count) + temp
                temp = prev[i]
                count =1
        out = out + str(count) + temp
        return out


if __name__ == "__main__":
    obj = Solution()
    n = 5
    out1 = obj.countAndSay(10)
    out2 = obj.countAndSay1(n)
    print(out1)
    print(out2)




