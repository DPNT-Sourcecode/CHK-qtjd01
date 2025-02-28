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

        counts = self._count_skus(basket.skus)
        counts = self._apply_free_items(counts, [('B', 'E', 2), ('M', 'N', 3), ('Q', 'R', 3)])
        group_total, counts = self._group_skus(counts, ['S', 'T', 'X', 'Y', 'Z'])
        remaining_total = self._calculate_remaining_total(counts)
        if remaining_total < 0:
            return -1

        total = group_total + remaining_total
        logger.info(f'Total price: {total}')
        return total

    def _count_skus(self, skus: str) -> dict:
        counts = {}
        for ch in skus:
            counts[ch] = counts.get(ch, 0) + 1
        return counts

    def _apply_free_items(self, counts: dict, items: list[tuple]) -> dict:
        for free_item, required_item, required_qty in items:
            free_count = counts.get(required_item, 0) // required_qty
            if free_item in counts:
                counts[free_item] = max(counts[free_item] - free_count, 0)
        return counts

    def _group_skus(self, counts: dict, group_skus: list) -> (int, dict):
        group_prices = []
        for sku in group_skus:
            if sku in counts:
                product = self.products.get(sku)
                for _ in range(counts[sku]):
                    group_prices.append(product.price)
                del counts[sku]

        group_total = 0

        if group_prices:
            group_prices.sort(reverse=True)
            while len(group_prices) >= 3:
                group_total += 45
                group_prices = group_prices[3:]
            group_total += sum(group_prices)
        return group_total, counts

    def _calculate_remaining_total(self, counts: dict) -> int:
        total = 0
        for sku, qty in counts.items():
            product = self.products.get(sku)
            if not product:
                logger.error(f'Invalid sku {sku}')
                return -1
            total += product.calculate_price(qty)
        return total


def checkout(arg) -> int:
    if isinstance(arg, list):
        skus = arg[0] if arg else ''
    elif isinstance(arg, str):
        skus = arg
    else:
        skus = str(arg)

    return Checkout().calculate_total(skus)


