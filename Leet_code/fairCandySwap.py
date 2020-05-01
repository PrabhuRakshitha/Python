class Solution:
    def fairCandySwap(self, A, B):
        diff = (sum(B) - sum(A))//2
        B = set(B)
        for a in A:
            if a + diff in B:
                return [a, a+diff]

def main():
    obj = Solution()
    A = [1,2,5]
    B = [2,4]
    print(obj.fairCandySwap(A,B))

main()