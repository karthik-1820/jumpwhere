qty = int(input("Enter quantity: "))
cost = qty * 100
if cost > 1000:
    cost *= 0.9
print("Total cost:",cost)
