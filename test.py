sell, buy = 0, 0
prices = [7, 1, 5, 3, 6, 4]
maximum = 0
j = 0
for i in range(len(prices)):
    if j < len(prices):
        j = i+1
        if prices[j] + prices[i] > maximum:
            maximum = prices[j]+prices[i]
        j += 1
        print(prices[i], prices[j], maximum)
