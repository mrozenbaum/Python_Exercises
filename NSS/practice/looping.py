#------- Lists

large_flowers = list()
flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
for f in flowers:
    large_flowers.append('a large ' + f)

print(large_flowers)


#------- Dictionaries

family = { 'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}
for key, value in family.items():
    print(key, value)

#family.values() will return values


#------- Sets

cars = { 'Lexus', 'Chevy', 'Jeep' }
for c in cars:
    print(c)


