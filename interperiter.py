from bitstring import BitArray 
import interperitercode

x = "error"

asordis = input("1: Assemble\n2: Dissassemble\nPlease enter 1 or 2: ")

if asordis == 1:
    x = "assemble"
if asordis == 2:
    x = "dissassemble"

inputfile = raw_input("Enter the file you would like to " + x + ": ")
outfile = raw_input("Enter the output file: ")


if asordis == 1:
    interperitercode.assemble(inputfile, outfile)
if asordis == 2:
    interperitercode.disassemble(inputfile, outfile)
print"---------------------------------\n\tFunction Complete\n---------------------------------"