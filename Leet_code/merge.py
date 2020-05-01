class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i=0
        del nums1[m:]
        while i < m:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j = j+1
                i = i+1
            else :
                i=i+1
        nums1.extend(nums2[j:])

        return nums1





def main():
    a=Solution()
    print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))

main()