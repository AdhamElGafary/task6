# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):

    def test_find_by_name(self):
        # Create and save a product with a known name
        known_name = fake.company()
        product = Product(name=known_name,
                          description=fake.text(max_nb_chars=200),
                          price=99.99,
                          sku=fake.uuid4(),
                          category=fake.word())
        product.save()  # Assuming the 'save' method persists the product

        # Simulate the "find by name" operation
        found_product = Product.find_by_name(known_name)  # Assuming 'find_by_name' method fetches product by name

        # Check that a product is found and the name matches the known name
        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.name, known_name)

if __name__ == '__main__':
    unittest.main()
