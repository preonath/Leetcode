#### Solution 1 ###

def maxProfit(prices):
    
    max_profit = 0
    min_price = prices[0]
    
    for i in prices[1:]:
        # print(i)
        if(i < min_price):
            min_price = i
        elif(max_profit < i - min_price):
            max_profit = i - min_price
    return(max_profit)

    
    if len(prices) == 0:
        return 0

prices = [7,1,5,6,4,3]
maxProfit(prices)


#### Solution 2 ###

def maxProfit(prices):
    buy_position = 0
    sell_position = 1
    maximum_profit= 0
    
    while(sell_position < len(prices)):
        current_profit = prices[sell_position]-prices[buy_position]
        
        if(prices[sell_position] > prices[buy_position] ):
            maximum_profit = max(current_profit,maximum_profit) 
        else:
            buy_position = sell_position
        sell_position +=1
    return(maximum_profit)

prices = [7,1,5,3,6,4]
maxProfit(prices)
