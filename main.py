def find_coins_greedy(amount):
    denominations = [50, 10, 5, 2, 1]
    result = {}
    
    for coin in denominations:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    
    return result


def find_min_coins(amount):
    denominations = [50, 10, 5, 2, 1]
    # Таблиця для зберігання мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    # Таблиця для зберігання вибору монет
    coin_used = [0] * (amount + 1)
    
    for coin in denominations:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}