class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

# Example of using the class
i = Item(10, 20)
print(i.price)  # Output: 10
print(i.weight)  # Output: 20
