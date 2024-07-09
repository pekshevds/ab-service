from pydantic import BaseModel


class Cart(BaseModel):
    cart_items: dict[str, float] = dict()


__all__ = (Cart,)
