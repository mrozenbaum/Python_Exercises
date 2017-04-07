# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("Honda")
showroom.add("Toyota")
showroom.add("Nissan")
showroom.add("Accord")

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("Accord")
print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Truck", "Car"})

# Using update(), add two more car models to your showroom with another set.
meg = {"Focus": "Civic"}.items()
for key,value in meg:
  showroom.update((key, value))
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Honda")
print(showroom)


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Accord", "Sedan", "OldCarOne", "OldCarTwo", "OldCarThree"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
shared_cars = showroom.intersection(junkyard)
print(shared_cars)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
all_cars = showroom.union(junkyard)
print(all_cars)

# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
for car in junkyard:
  all_cars.discard(car)
print(all_cars)


