# Create a tuple named zoo that contains your favorite animals.
zoo = ("Monkey", "Dolphin", "Ant", "Elephant")


# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("Elephant"))


# Determine if an animal is in your tuple by using for value in tuple.
for value in zoo:
  print(value)


# Create a variable for each of the animals in your tuple with this cool feature of Python.
(meg, ducharme, baltimore, maryland) = zoo
print(meg)
print(ducharme)
print(baltimore)

# Convert your tuple into a list.
zoo = list(zoo)
print(type(zoo))


# Use extend() to add three more animals to your zoo.
zoo.extend(["Bug", "Tiger", "Bird"])
print(zoo)

# Convert the list back into a tuple.
zoo = tuple(zoo)
print(type(zoo))
