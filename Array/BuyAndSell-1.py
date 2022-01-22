"""Input: prices = [0,1,5,3,6,4,7]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell."""

def buySell(nums):
    mini=nums[0]
    profit=0
    max_profit=0
    for i in nums:
        mini=min(mini,i)
        profit=i-mini
        max_profit=max(profit,max_profit)
    return max_profit

if __name__=='__main__':
    prices = [0,1,5,3,6,4,7]
    print(buySell(prices))