def test_create_product(self):
    product = Product(name="TestProduct", category="TestCategory", price=100, availability=True)
    product.save()
    self.assertEqual(Product.objects.count(), 1)

def test_find_by_name(self):
    product = ProductFactory(name="TestProduct")
    product.save()
    found = Product.find_by_name("TestProduct")
    self.assertIsNotNone(found)
