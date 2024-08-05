from django.test import TestCase
from catalog_app.models import Good


class CartTest(TestCase):
    def setUp(self):
        self._good1 = Good.objects.create(name="good1")
        self._good2 = Good.objects.create(name="good2")
        self._good3 = Good.objects.create(name="good3")

    def test_cart(self):
        resp = self.client.get("/api/v1/cart/")
        self.assertEqual(resp.status_code, 200)

    def test_add_cart(self):
        resp = self.client.get(f"/api/v1/cart/add/?id={self._good1.id}")
        self.assertEqual(resp.status_code, 200)

        cart = resp.data
        self.assertIsNotNone(cart, None)
        self.assertEqual(len(cart.cart_items), 1)

        resp = self.client.get(f"/api/v1/cart/add/?id={self._good2.id}")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(f"/api/v1/cart/add/?id={self._good3.id}")
        self.assertEqual(resp.status_code, 200)

    def test_set_cart(self):
        resp = self.client.get(f"/api/v1/cart/set/?id={self._good1.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(f"/api/v1/cart/set/?id={self._good2.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(f"/api/v1/cart/set/?id={self._good3.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)

        cart = resp.data
        self.assertIsNotNone(cart, None)
        self.assertEqual(cart.cart_items.get(str(self._good3.id)), 5.0)
        self.assertNotEqual(cart.cart_items.get(str(self._good3.id)), 1.0)

    def test_delete_cart(self):
        resp = self.client.get(f"/api/v1/cart/delete/?id={self._good1.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(f"/api/v1/cart/delete/?id={self._good2.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(f"/api/v1/cart/delete/?id={self._good3.id}&qnt=5")
        self.assertEqual(resp.status_code, 200)

    def test_clear_cart(self):
        resp = self.client.get("/api/v1/cart/clear/")
        self.assertEqual(resp.status_code, 200)
        cart = resp.data
        self.assertEqual(len(cart.cart_items), 0)
