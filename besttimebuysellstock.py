class Solution:
    def maxProfit(self, prices):
        import sys
        """
        Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete at most two transactions.
        
        Note:
        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        """
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        maxprev = 0
        sell1 = 0
        sell2 = 0
        buy1 = -sys.maxsize
        buy2 = -sys.maxsize
        for i in range(len(prices)):
            buy1 = buy1 if buy1>-prices[i] else -prices[i]
            sell1 = sell1 if sell1>buy1+prices[i] else buy1+prices[i]
            buy2 = buy2 if buy2 > sell1 - prices[i] else sell1 - prices[i]
            sell2 = sell2 if sell2 > buy2 + prices[i] else buy2 + prices[i]

        return sell1 if sell1>sell2 else sell2


s = Solution()
print(s.maxProfit([2,1,2,0,1]))