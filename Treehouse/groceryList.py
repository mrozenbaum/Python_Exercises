import pdb

groceryList = []

print("""
--------- GROCERY LIST ---------
------- [A] Add New Items ------
------- [B] Delete an Item ------
------- [C] Show Items ---------
------- [D] Exit ---------------
  """)

def showList():
  print(", ".join(groceryList))

def addGroceries(groceryToAdd):
  groceryList.append(groceryToAdd)
  showList()

def task():

  groceryItem = input("What would you like to do? ")

  if groceryItem == "B":
    showList()
    itemToDelete = input("What do you want to remove? ")
    groceryList.remove(itemToDelete)
    showList()
    task()
  if groceryItem == "C":
    showList()
    task()
  if groceryItem == "D":
    print("Things to get at the groery store are " + ", ".join(groceryList))
    exit()
  if groceryItem == "A":
    grocery_to_add = input("What would you like to add? ")
    addGroceries(grocery_to_add)
    task()

task()
