new_list = []
values = [{"name":"Meg", "food":"Sushi"},{"name":"Sarah", "food":"Sandwiches"}, {"name":"Dean", "food": "Donuts"}]

def string_factory(values):
    for dictionary in values:
        new_list.append("Hi, I'm {} and I love to eat {}!".format(dictionary['name'], dictionary['food']))
    print(new_list)

string_factory(values)
