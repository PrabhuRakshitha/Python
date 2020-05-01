class Solution(object):
    def maxProfitv1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        max_profit=0
        min_index
        for i in range(1, len(prices)):
            if prices[i] < prices[min_index]:
                min_index =i
            max_profit = max(max_profit,prices[i]-min_index)

        return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice =-1
        maxprofit= 0
        for cost in prices:
            if minprice ==-1 or minprice > cost:
                minprice = cost
            else:
                maxprofit = max( maxprofit, maxprofit+(cost -minprice))
                minprice =cost

        return maxprofit


if __name__ == '__main__':
    obj = Solution()
    out=obj.maxProfit([7,6,4,3,1])
    print(out)






