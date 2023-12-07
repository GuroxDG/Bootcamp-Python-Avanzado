'''
Lists
'''

# Iterar por For Loop
squares = []
for i in range(10):
    squares.append(i * i)

print(squares)

# Map
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08

def get_price_with_tax(txns):
    return txns * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, txns)
print(list(final_prices))

# List Comprenhension
squares = [i * i for i in range(10)]
print(squares)