class Products:
    def __init__(self, sku: str, price: int, special_qty: int = None, special_price: int = None):
        self.sku = sku
        self.price = price
        self.special_qty = special_qty
        self.special_price = special_price

    def calculate_price(self, qty: int) -> int:
        if self.special_qty and self.special_price:
            nums_specials = qty // self.special_qty
            remaining = qty % self.special_qty
            return nums_specials * self.special_price + remaining * self.price
        return qty * self.price