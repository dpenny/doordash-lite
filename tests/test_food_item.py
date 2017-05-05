from ddl.models import FoodItem


def test_unicode():
  apple = FoodItem(name='apple')
  assert apple.name == 'apple'