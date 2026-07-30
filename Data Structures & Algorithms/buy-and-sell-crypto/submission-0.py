""" 
implicit sliding window, see DavidPersonalLC package 
for claude's solution which is cleanest.


iterate price:
if the price is new low, move left pointer here
if not, may sell it here, update profit


[4,6,2,8]
 l

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf') # (left edge)

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
        