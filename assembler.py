import enginecode
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename

Tk().withdraw()

x = "error"

while x == "error":
    #asordis means assembler or disassembler
    asordis = input("1: Assemble\n2: Disassemble\nPlease enter 1 or 2: ")

    if asordis == 1:
        x = "assemble"
    if asordis == 2:
        x = "disassemble"
    if asordis == "error":
        print "Put in 1 or 2 you goddamn commie"

#this means quite literally what it is
print "Choose the file you would like to input"
inputfile = askopenfilename()
print "Enter the name of the output file"
outfile = asksaveasfilename()

#basically does the function that the user selects
if asordis == 1:
    enginecode.wipe(outfile)
    enginecode.assemble(inputfile, outfile)

if asordis == 2:
    enginecode.wipe(outfile)
    enginecode.disassemble(inputfile, outfile)
    

#looks fancy
print"---------------------------------\n\tFunction Complete\n---------------------------------"
