class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row =['']*numRows
        index =0
        godown = False
        for i in s:
            print(i)
            print(index)
            row[index] =row[index]+i
            if index ==0 or index == numRows-1:
                godown = not godown

            if godown:
                index =index +1
            else:
                index = index-1
        out =''

        for sub in row:
            out = out+sub

        return out




if __name__ =="__main__":
    obj =Solution()
    out= obj.convert('abcabcde',3)
    print(out)