import factory
from myapp.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    category = factory.Faker("word")
    price = factory.Faker("random_number", digits=4)
    availability = factory.Faker("boolean")
