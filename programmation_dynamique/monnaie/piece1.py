def change_render(p, price, given_money):
    change = given_money - price
    if change < 0:
        raise Exception("the price cannot be greater than the given money")
    else:
        pos_m = []  # En gros ça donne les pièce inférieur au montant de change
        pos_m = sorted([i for i in p if i <= change])
        pos_t = []
