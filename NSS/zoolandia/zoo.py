#------------- Zoos
class Zoo:
    """Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    """
    def __init__(self, name):
        self.zoo_name = name
        self.animals = set()
        self.habitats = set()
        self.visitors = list()
        self.habitat_population = dict()


    def build_habitat(self, habitat):
        """Adds tuples to the habitats set in the format (name, type)

        Method arguments:
        -----------------
        name(string) -- The marketing name of the habitat
        type(string) -- The type of habitat (e.g. Saltwater, Savanna, Swamp, etc.)
        """

        self.habitats.add(habitat)


    def sell_family_ticket(self, family):
        """Adds an entire family to the list of visitors

        Method argument:
        -----------------
        family(list) -- A list of people in a family of visitors
        """

        self.visitors.extend(family)


    def purchase_animal(self, animal):
        """Add an animal to the zoo

        Method arguments:
        -----------------
        type(string) -- The type of animal to add
        name(string) -- The given name of the animal
        """

        self.animals.add(animal)

    def animal_report(self):
        for habitat in self.habitats:
            print(habitat.marketing_name)
            print("--------------------")
            for animal in self.animals:
                if animal.habitat is habitat:
                    print(animal.name + "\n")


    def list_animals(self):
        """Lists all animals in the zoo
        Method arguments:
        n/a
        """

        [print("{} the {}".format(animal.name, animal.type)) for animal in self.animals]
        #.items() is a dictionary command

