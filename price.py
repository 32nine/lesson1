price = 100
discount = 5
price_with_discount = price - price * discount / 100
print(price_with_discount)

def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    sum = one + delimiter + two
    return sum.upper()


print(get_sum('learn','python'))


def format_price(price):
    price = int(price)
    result = f"Цена {price}.руб"
    return result

print(format_price(56.24))

