class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        alpha ={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

        temp=dict()
        for word in strs:
            key =1
            for i in word:
                key =  alpha[i] *key

            if key in temp:
                temp[key].append(word)
            else:
                temp[key]=[word,]
        print(temp)

        out=[]
        for values in temp.values():
            out.append(values)
        return out



if __name__ == '__main__':
    obj = Solution()
    strs = ["db","ah","pew","duh","may","ill","buy","bar","max","doc"]
    out = obj.groupAnagrams(strs)
    print (out)