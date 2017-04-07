# Use append() to add Jupiter and Saturn at the end of the list.
planets = list()
planets.append("Jupiter")
planets.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planets.extend(["Planet1", "Planet2"])
print(planets)

# Use insert() to add Earth, and Venus in the correct order.
planets.insert(4, "Earth")
planets.insert(5, "Venus")
print(planets)

# Use append() again to add Pluto to the end of the list.
planets.append("Pluto")


# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planets[1:]
print(rocky_planets)


# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del rocky_planets[5]
# del rocky_planets[planets.index("Pluto")]
print(rocky_planets)


# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
print(planets)
another_list = [("Craft1","Saturn", "Pluto"),("Craft2","Moon", "Venus"),("Craft3","Venus")]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.
for planet in planets:
  for thing in another_list:
    if planet in thing:
      print(planet+" has been visited by "+str(thing[0]))

