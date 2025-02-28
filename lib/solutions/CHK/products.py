class Product:
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


class MultiOfferProduct(Product):
    def __init__(self, sku: str, price: int, offers: list):
        super().__init__(sku, price, price)
        self.offers = offers

    def calculate_price(self, qty: int) -> int:
        dp = [float('inf')] * (qty + 1)
        dp[0] = 0
        for i in range(1, qty + 1):
            dp[i] = dp[i - 1] + self.price
            for offer_qty, offer_price in self.offers:
                if i >= offer_qty:
                    dp[i] = min(dp[i], dp[i - offer_qty] + offer_price)
        return dp[qty]

