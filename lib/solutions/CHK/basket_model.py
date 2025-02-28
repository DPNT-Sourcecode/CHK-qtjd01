from pydantic import BaseModel, field_validator


class BasketModel(BaseModel):
    skus: str

    @field_validator("skus")
    def validate_skus(cls, value: str) -> str:
        allowed = {'A', 'B', 'C', 'D', 'E'}
        if not isinstance(value, str):
            raise ValueError('skus must be a string')
        for ch in value:
            if ch not in allowed:
                raise ValueError(f'Invalid sku {ch}')
        return value

