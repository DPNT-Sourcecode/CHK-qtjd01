from pydantic import BaseModel, validator

class BasketModel(BaseModel):
    basket: str

    @validator('basket')
    def check_basket(cls, value):
        if not all([x.isalpha() for x in value]):
            raise ValueError("Basket should contain only alphabets")
        return value
