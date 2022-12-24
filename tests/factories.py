import factory
import factory.fuzzy
from django.contrib.auth import get_user_model

from nyrkes.models import Organization


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.first_name}.{obj.last_name}@example.com")
    password = factory.fuzzy.FuzzyText()


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Faker("company")
    alt_name = factory.Faker("company")
    owner = factory.SubFactory(UserFactory)
