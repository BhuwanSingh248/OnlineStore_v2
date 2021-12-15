from typing import Text
import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecomm_apps.Inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="category_???????")
    slug = fake.lexify(text="category_??????")


register(CategoryFactory)
