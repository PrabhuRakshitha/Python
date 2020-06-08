class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        sorted_list = []
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                sorted_list.append(nums1[i])
                i = i + 1
            else:
                sorted_list.append(nums2[j])
                j = j + 1

        while i < n:
            sorted_list.append(nums1[i])
            i = i + 1

        while j < m:
            sorted_list.append(nums2[j])
            j = j + 1

        mid = (n + m) // 2
        if (n + m) % 2 == 0:
            median = (sorted_list[mid] + sorted_list[mid - 1]) / 2
        else:
            median = sorted_list[mid]

        return median


if __name__ =="__main__":
    obj = Solution()

    out =obj.findMedianSortedArrays([1,2],[3,4])
    print(out)




