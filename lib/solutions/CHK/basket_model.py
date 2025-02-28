from pydantic import BaseModel, field_validator
from solutions.CHK.product_catalog import ALLOWED_SKUS


class BasketModel(BaseModel):
    skus: str

    @field_validator("skus")
    def validate_skus(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError('skus must be a string')
        for ch in value:
            if ch not in ALLOWED_SKUS:
                raise ValueError(f'Invalid sku {ch}')
        return value
