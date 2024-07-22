from typing import Sequence
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from cart_app.schemas import Cart
from cart_app.models import Recipient
from catalog_app.models import Good


def get_cart(request: HttpRequest) -> Cart:
    cart_json = request.session.get("cart")
    if cart_json:
        cart = Cart.model_validate(cart_json)
    else:
        cart = Cart()
        save_cart(request, cart)
    return cart


def add_to_cart(request: HttpRequest) -> None:
    good = get_object_or_404(Good, id=request.GET.get("id"))
    qnt = float(request.GET.get("qnt", 1.0))

    cart = get_cart(request)
    res = cart.cart_items.get(str(good.id))
    if not res:
        cart.cart_items[str(good.id)] = 0
    cart.cart_items[str(good.id)] += qnt
    save_cart(request, cart)


def set_to_cart(request: HttpRequest) -> None:
    good = get_object_or_404(Good, id=request.GET.get("id"))
    qnt = float(request.GET.get("qnt", 1.0))

    cart = get_cart(request)
    cart.cart_items[str(good.id)] = qnt
    save_cart(request, cart)


def delete_from_cart(request: HttpRequest) -> None:
    good = get_object_or_404(Good, id=request.GET.get("id"))
    qnt = float(request.GET.get("qnt", 1.0))

    cart = get_cart(request)
    res = cart.cart_items.get(str(good.id))
    if res:
        if res <= qnt:
            del cart.cart_items[str(good.id)]
        else:
            cart.cart_items[str(good.id)] -= qnt
    save_cart(request, cart)


def clear_cart(request: HttpRequest) -> None:
    cart = Cart()
    save_cart(request, cart)


def save_cart(request: HttpRequest, cart: Cart) -> None:
    request.session["cart"] = cart.model_dump()


def send_cart(cart: Cart) -> bool:
    recipient_list = [recipient.email for recipient in Recipient.objects.all()]
    result = 0
    if len(recipient_list) > 0:
        html_message = "<h1>message<h1>"
        result = send_mail(
            "Корзина",
            "Сообщение",
            None,
            recipient_list=recipient_list,
            html_message=html_message,
        )
    return True if result == 1 else False


__all__: Sequence[str] = (
    "get_cart",
    "add_to_cart",
    "delete_from_cart",
    "clear_cart",
    "set_to_cart",
    "send_cart",
)
