c = input("How many copies are you purchasing? :") # c = number of copies purchased
c = int(c)
book_price = 24.95 * 0.6 * c
if c == 0:
    shipping_cost = 0
else:
    shipping_cost = 3 + 0.75 * (c-1)
total_cost = book_price + shipping_cost
print(f"Total cost = ${total_cost:.2f}")
