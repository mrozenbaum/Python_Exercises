from sys import argv

#as arguments to the terminal, pass in the script to be read, and the inputfile (text.txt)
script, input_file = argv

#this function will take a file and read through and print it to the console
def print_all(f):
  print(f.read())

#this will take realign the head to the beginning of the file before it starts to print what is asked within the function
#seek will reset the head to the beginning of the file via the 0 -- same as rewind (above)
def rewind(f):
  f.seek(0)

#print a line, the one that is passed in, in the file that is passed in
def print_a_line(line_count, f):
  print(line_count, f.readline())

#open the input_file and assign it to current_file variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
