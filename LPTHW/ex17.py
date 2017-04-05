#from sys - the terminal, import the argument variables
from sys import argv
#not sure what this does?
from os.path import exists

#the name of the file, another file chosen by the user and typed in the command line, another file chosen by the user and typed into the commandline
script, from_file, to_file = argv

#print the string formatted to include the variables
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

#to do in one line
indata = open(from_file).read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# in_file.close()
