
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count =0
        count_ele = dict()
        for i in arr:
            if i in count_ele:
                count_ele[i] += 1
            else:
                count_ele[i] = 1
        for key in count_ele:
            try:
                if count_ele[key+1]:
                    count = count + count_ele[key]
            except KeyError:
                pass


        return count


if __name__ == '__main__':
    obj = Solution()
    arr = [1,1,2,2]

    out = obj.countElements(arr)
    print (out)