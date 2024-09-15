class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        return self._calories is None or self._calories < 200

    def is_delicious(self):
        return True
class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != "black licorice"


dessert1 = Dessert("Ice Cream", 300)
print(dessert1.name)
print(dessert1.calories)
print(dessert1.is_healthy())
print(dessert1.is_delicious())

dessert2 = Dessert("Fruit Salad", 150)
print(dessert2.name)
print(dessert2.calories)
print(dessert2.is_healthy())
print(dessert2.is_delicious())

jelly_bean1 = JellyBean("Strawberry", 50, "strawberry")
print(jelly_bean1.name)
print(jelly_bean1.calories)
print(jelly_bean1.flavor)
print(jelly_bean1.is_healthy())
print(jelly_bean1.is_delicious())

jelly_bean2 = JellyBean("Black Licorice", 75, "black licorice")
print(jelly_bean2.name)
print(jelly_bean2.calories)
print(jelly_bean2.flavor)
print(jelly_bean2.is_healthy())
print(jelly_bean2.is_delicious())


