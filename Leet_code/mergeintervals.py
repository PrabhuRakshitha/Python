class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out =[]
        if len(intervals) <=1:
            return intervals
        new_interval = intervals[0]

        for item in intervals:
            if min(new_interval) <= min(item)<= max(new_interval):
                new_interval =[min(new_interval), max(max(new_interval), max(item))]
            else:
                out.append(new_interval)
                new_interval = item
        out.append(new_interval)
        return out

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        out = []
        if len(intervals) == 0:
            return [newInterval]
        new_interval = newInterval

        for item in intervals:
            if min(item) <= min(new_interval) <= max(item):
                new_interval = [min(item), max(new_interval)]
            elif min(item) <= max(new_interval)<= max(item):
                new_interval = [min(new_interval), max(item)]
            elif min(new_interval) <= min(item) <= max(new_interval):
                continue
            elif min(item) > max(new_interval)
                
            else:
                out.append(item)
        return out


if __name__ =="__main__":
    obj = Solution()
    intervals = [[1,3],[6,9]]
    new_int=[2,5]
    out = obj.insert(intervals,new_int)
    print(out)
