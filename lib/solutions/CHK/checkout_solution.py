from logger import get_logger
from solutions.CHK.products import Product
from solutions.CHK.basket_model import BasketModel
from pydantic import ValidationError

logger = get_logger(__name__)


# noinspection PyUnusedLocal
# skus = unicode string
class Checkout:
    def __init__(self):
        self.products = {
            'A': Product('A', 50, 3, 130),
            'B': Product('B', 30, 2, 45),
            'C': Product('C', 20),
            'D': Product('D', 15)
        }

    def calculate_total(self, skus: str) -> int:
        try:
            basket = BasketModel(skus=skus)
        except ValidationError as e:
            logger.error(f'Invalid skus: {e}')
            return -1

        counts = {}
        for ch in basket.skus:
            counts[ch] = counts.get(ch, 0) + 1

        total = 0
        for sku, qty in counts.items():
            product = self.products.get[sku]
            if not product:
                logger.error(f'Invalid sku {sku}')
                return -1
            product_total = product.calculate_price(qty)
            logger.info(f'{sku}: {qty} x {product.price} = {product_total}')
            total += product_total

        logger.info(f'Total: {total}')
        return total


def checkout(skus: str) -> int:
    return Checkout().calculate_total(skus)


