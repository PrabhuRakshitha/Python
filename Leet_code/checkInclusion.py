class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) == len(s2):
            if (''.join(sorted(s1)))!=(''.join(sorted(s2))):
                return False

        x = []
        s1 =list(s1)
        self.permute(s1, 0, len(s1)-1, x)
        for exp in x:
            if exp in s2:
                return True
        return False

    def permute(self, s1, l, r, x):
        if l == r:
            temp=''.join(s1)
            x.append(temp)
        else:
            for i in range(l, r+1):
                s1[l], s1[i] = s1[i], s1[l]
                self.permute(s1, l+1, r, x)
                s1[l], s1[i] = s1[i], s1[l]



class Solution2(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) == len(s2):
            if (''.join(sorted(s1)))!=(''.join(sorted(s2))):
                return False
        x = []
        s1 = list(s1)
        flag = False
        flag = self.permute(s1, 0, len(s1) - 1, s2)
        print('printing flag :',flag)

        if flag:
            return True
        else:
            return False

    def permute(self, s1, l, r, s2):
        if l == r:
            temp = ''.join(s1)
            print(temp)
            if temp in s2:
                print('inside if')
                return True

        else:
            for i in range(l, r + 1):
                s1[l], s1[i] = s1[i], s1[l]
                flag = self.permute(s1, l + 1, r, s2)
                if flag:
                    return True
                s1[l], s1[i] = s1[i], s1[l]


def main():
    a=Solution()
    s1 ='dinitrophenylhydrazine'
    s2='acetylphenylhydrazine'
    print(a.checkInclusion(s1,s2))

main()

