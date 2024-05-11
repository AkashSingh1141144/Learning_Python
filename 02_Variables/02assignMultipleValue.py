#  Many values to Multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#  One value to Multiple variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

#  Unpack a collection
"""
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""

cars = ['Ford', 'Volvo', 'BMW']
x, y, z = cars
print(x)
print(y)
print(z)


x = 5
y = 10
print(x + y)