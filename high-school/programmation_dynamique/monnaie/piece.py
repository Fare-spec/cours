def machine_bruteforce(price, enter, money_allowed):
    assert (
        enter >= price
    ), "The entered amount must be greater than or equal to the price"
    change = enter - price
    if change == 0:
        return [[]]

    results = []

    def brute(current_combination, total):
        if total == change:
            results.append(current_combination.copy())
            return
        if total > change:
            return

        for coin in money_allowed:
            current_combination.append(coin)
            brute(current_combination, total + coin)
            current_combination.pop()

    brute([], 0)
    return results
