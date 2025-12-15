# this is what we will use for the video intro to dictionaries

# dictionary = a collection of {key:value} pairs ordered and changable, no duplicates

capitals = {"USA":"Washington DC", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}

print(dir(capitals))
# print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(values)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")










