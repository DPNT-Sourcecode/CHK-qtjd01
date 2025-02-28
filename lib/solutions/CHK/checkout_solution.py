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

        for free_item, required_item, required_qty in [('B', 'E', 2), ('M', 'N', 3), ('Q', 'R', 3)]:
            free_count = counts.get(required_item, 0) // required_qty
            if free_item in counts:
                counts[free_item] = max(counts[free_item] - free_count, 0)

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
