class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit=sell-buy (buy at a lower price and sell at higher)
        maxP=0
        minBuy=prices[0]
        for sell in prices:
            maxP=max(maxP,sell-minBuy)
            minBuy=min(minBuy,sell)
        return maxP
