my_family = {
    'sister': {
        'name': 'Jennifer',
        'age': 25
    },
    'mother': {
        'name': 'Judy',
        'age': 66
    },
    'father': {
        'name': 'Bob',
        'age': 66
    },
    'brother': {
        'name': 'Jimmy',
        'age': 31
    }
}

# for key,value in my_family.items():
#     print(my_family[key]['name'] + " is my " + key + " and is " + str(my_family[key]['age']) + " years old.")

#dictionary comprehension
{print(my_family[key]['name'] + " is my " + key + " and is " + str(my_family[key]['age']) + " years old.") for key, value in my_family.items()}
