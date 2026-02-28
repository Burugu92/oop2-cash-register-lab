class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount  # validate via property
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    # Discount property validation
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
     if self.discount == 0:
        print("There is no discount to apply.")
        return
     self.total = self.total * (1 - self.discount / 100)
    # Format total for message
     if self.total == int(self.total):
        total_str = f"${int(self.total)}"
     else:
        total_str = f"${self.total:.2f}"
     print(f"After the discount, the total comes to {total_str}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            self.items.pop()  # remove from end, safer than remove()