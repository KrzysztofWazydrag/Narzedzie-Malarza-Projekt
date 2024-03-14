def calculate_brutto(netto:float, vat:float=0.23)->float:
    return netto * (1 + vat)

def calculate_netto(brutto:float, vat:float=0.23)->float:
    return brutto / (1 + vat)

def calculate_discount(total: float, discounts:list)->float:
    for discount in discounts:
        total -= total * discount

    return total