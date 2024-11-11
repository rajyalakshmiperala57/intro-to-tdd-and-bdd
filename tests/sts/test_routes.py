def test_get_product(self):
    product = ProductFactory()
    product.save()
    response = self.client.get(f"/products/{product.id}")
    self.assertEqual(response.status_code, 200)
