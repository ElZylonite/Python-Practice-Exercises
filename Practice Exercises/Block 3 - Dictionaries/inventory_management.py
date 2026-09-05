inventory = {
    "shirts": 12,
    "pants": 3,
    "shoes": 4,
    "hats": 8,
    "belts": 2
}

buy = []

for product, amount in inventory.items():
    if amount < 5:
        buy.append(product)

print("You need to buy more: ", buy)
