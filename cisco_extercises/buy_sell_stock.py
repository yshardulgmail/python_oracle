def maxProfit(prices):
        lowest_day = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if lowest_price > prices[i]:
                lowest_price = prices[i]
                lowest_day = i

        highest_price = lowest_price
        for i in range(lowest_day, len(prices)):
            if highest_price < prices[i]:
                highest_price = prices[i]

        return highest_price - lowest_price


prices = [7,1,5,3,6,4]
print("Maximum Profit: ", maxProfit(prices))