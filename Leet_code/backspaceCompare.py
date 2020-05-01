class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_list=[]
        t_list=[]
        for a in S:
            if a=='#':
                if s_list:
                    s_list.pop()
                else:
                    continue
            else:
                s_list.append(a)

        for b in T:
            if b=='#':
                if t_list:
                    t_list.pop()
                else:
                    continue
            else:
                t_list.append(b)
        return s_list == t_list


if __name__ == '__main__':
    obj = Solution()
    S = "y#fo##f"
    T = "y#f#o##f"
    out = obj.backspaceCompare(S,T)
    print (out)