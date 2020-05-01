class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        prev = A[0]
        if A[0] > A[-1]:
            flag = 'down'
        else:
            flag = 'up'
        for i in range(1,len(A)):
            if flag =='up' and A[i] < prev:
                return False
            if flag =='down' and A[i] > prev:
                return False
            prev = A[i]
        return True


def main():
    obj = Solution()
    A = [1,3,2]
    print(obj.isMonotonic(A))

main()
