from bitstring import BitArray 
import interperitercode

x = "error"

while x == "error":
    #asordis means assembler or disassembler
    asordis = input("1: Assemble\n2: Disassemble\nPlease enter 1 or 2: ")

    if asordis == 1:
        x = "assemble"
    if asordis == 2:
        x = "disassemble"
    else:
        print "Put in 1 or 2 you goddamn commie"
#this means quite literally what it is
inputfile = raw_input("Enter the file you would like to " + x + ": ")
outfile = raw_input("Enter the output file: ")

#basically does the function that the user selects
if asordis == 1:
    interperitercode.assemble(inputfile, outfile)
if asordis == 2:
    interperitercode.disassemble(inputfile, outfile)
#looks fancy
print"---------------------------------\n\tFunction Complete\n---------------------------------"