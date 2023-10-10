from collections import OrderedDict
fruits_type = OrderedDict([
    ("Apple",200),
    ("Watermelon",150),
    ("Grapes",100),
    ("Mangoes",100)

])
print(fruits_type)
for key, value in fruits_type.items():
    print(key, value)
