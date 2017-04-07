from animal import *
from habitat import *
from zoo import *



island = Habitat("Galapagos", "Island")
jungle = Habitat("Dark Continent", "Jungle")
savannah = Habitat("Safari", "Savannah")




tommy = Animal("Tommy", "Tortoise")
tommy.habitat = island

chester = Animal("Chester", "Cheetah")
chester.habitat = savannah

horton = Animal("Horton", "Elephant")
horton.habitat = jungle

danny = Animal("Danny", "Dodo")
danny.habitat = island




a_zoo = Zoo("Zoolandia")

a_zoo.purchase_animal(tommy)
a_zoo.purchase_animal(horton)
a_zoo.purchase_animal(chester)
a_zoo.purchase_animal(danny)

a_zoo.build_habitat(island)
a_zoo.build_habitat(jungle)
a_zoo.build_habitat(savannah)

a_zoo.list_animals()

print(a_zoo.list_animals.__doc__) # To view the docstring for the method
# print(dir(a_zoo))
