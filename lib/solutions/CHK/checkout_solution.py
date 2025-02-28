from logger import get_logger
from solutions.CHK.product_catalog import PRODUCT_CATALOG
from solutions.CHK.basket_model import BasketModel
from pydantic import ValidationError

logger = get_logger(__name__)


# noinspection PyUnusedLocal
# skus = unicode string
class Checkout:
    def __init__(self):
        self.products = PRODUCT_CATALOG

    def calculate_total(self, skus: str) -> int:
        try:
            basket = BasketModel(skus=skus)
        except ValidationError as e:
            logger.error(f'Invalid skus: {e}')
            return -1

        counts = {}
        for ch in basket.skus:
            counts[ch] = counts.get(ch, 0) + 1

        free_b = counts.get('E', 0) // 2
        if 'B' in counts:
            counts['B'] = max(counts['B'] - free_b, 0)

        total = 0
        for sku, qty in counts.items():
            product = self.products.get(sku)
            if not product:
                logger.error(f'Invalid sku {sku}')
                return -1
            product_total = product.calculate_price(qty)
            logger.info(f'{sku}: {qty} x {product.price} = {product_total}')
            total += product_total

        logger.info(f'Total: {total}')
        return total


def checkout(arg) -> int:
    if isinstance(arg, list):
        skus = arg[0] if arg else ''
    elif isinstance(arg, str):
        skus = arg
    else:
        skus = str(arg)

    return Checkout().calculate_total(skus)

