#Array Trsverding:

from ast import Del


fruits = ["Banana", "Orange", "Apple", "Mango", "Grapes"]

for i, fruit in enumerate(fruits, start=0):
    print(i, "->", fruits)
print("/n")


# Array Insertion:
fruits.insert(2, "Pineapple")
for i, fruit in enumerate(fruits, start=0):
    print(i, "->", fruits)
print("/n")

# Array Deletion:

del fruits[1]
for i, fruit in enumerate(fruits, start=0):
    print(i, "->", fruits)



# Array Searching:
print(fruits.index("Apple"))
print(fruits.index("Grapes"))
print("/n")


# Array Sorting:

salaries = [1000, 2000, 3000, 4000, 5000]
for i, salary in enumerate(salaries, start=0):
    print(i, "->", salaries)

