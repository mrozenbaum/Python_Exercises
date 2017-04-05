def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man that's enough for a party!")
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


number_of_cheese = input("enter a number of cheese")
number_of_crackers = input("enter a number of crackers")
print(cheese_and_crackers(number_of_cheese, number_of_crackers))


# last_name = "Ducharme"

# def whats_yo_name(first_name, last_name):
#   print(f"Hello! {first_name}!")
#   input("What is you last name?")
#   print(f"{last_name} is a cool last name!")


# whats_yo_name("meg", last_name)


# user_input = input("type whats_yo_name")
# print(user_input)
