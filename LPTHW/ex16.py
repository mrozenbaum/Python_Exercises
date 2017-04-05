from sys import argv

# the arguments that are being passed in - script is the script that is running, and filename is ex15_sample
script, filename = argv

# print, but also format the string with the variable passed in
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN")

# input starts with a ? and waits for the user to type something
input("?")

# target is a variable that is holding the file that is open
print("Opening the file...")
# open the file and write
target = ex15_sample.txt
target.open("w")

target = open(filename, "w")


print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
