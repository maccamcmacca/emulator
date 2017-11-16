from bitstring import BitArray 

#dissassembles binary files
def disassemble(inputfile, outputfile):
    with open(inputfile) as f:
        content = f.readlines()
    #the value in strip is what characters are ommited during the read
    content = [x.strip() for x in content]


    for w in range(len(content)):
        
        s = content[w]
        
        readit = open(inputfile, "r")
        for line in readit:
            #gets every character past the 3rd
            r = s[3:]
            b = BitArray(bin=r)
        #append so that everything is looped and written
        writeit = open(outputfile, "a")
        #if statements that checks for the opcodes
        if s[:3] == "000":
            s = "JMP "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)
        
        if s[:3] == "100":
            s = "LDN "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)
        
        if s[:3] == "110":
            s = "STO "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)

        if s[:3] == "001":
            s = "SUB "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)

        if s[:3] == "011":
            s = "STP "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)
        
        if s[:3] == "111":
            s = "MUL "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)

        if s[:3] == "101":
            s = "DIV "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)

        if s[:3] == "010":
            s = "ADD "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(b.uint))
            writeit.writelines(l)
#assembles assembly code into binary
def assemble(inputfile, outputfile):
    with open(inputfile) as f:
        content = f.readlines()
    #the value in strip is what characters are ommited during the read
    content = [x.strip(" ") for x in content]

    for w in range(len(content)):
        #sets things up, also makes the binary correctly inputed
        s = content[w]
        r = int(s[3:])
        b = "{0:b}".format(r)
        #append so that everything is looped and written
        writeit = open(outputfile, "a")
        #if statements that changes assembly to opcodes
        if s[:3] == "JMP":
            s = "000"
            writeit.write(s)
        
        if s[:3] == "LDN":
            s = "100"
            writeit.write(s)
        
        if s[:3] == "STO":
            s = "110"
            writeit.write(s)
            

        if s[:3] == "SUB":
            s = "001"
            writeit.write(s)
            

        if s[:3] == "STP":
            s = "011"
            writeit.write(s)
        
        if s[:3] == "MUL":
            s = "111"
            writeit.write(s)

        if s[:3] == "DIV":
            s = "101"
            writeit.write(s)

        if s[:3] == "ADD":
            s = "010"
            writeit.write(s)
        #adds the decimal codes in binary following the opcode
        writeit.write(str(b).zfill(5))
        writeit.write("\n")

#wipes a file
def wipe(inputfile):
    s = open(inputfile, "w")
    s.writelines("")

def engine(inputfile):
    with open(inputfile) as l:
        content = l.readlines()
    
    content = [x.strip() for x in content]
    print content
    counter = 0
    memory = 0

    while True:
        for w in range(len(content)):
            r = content[w]
            opcode = r[:3]
            operand = r[3:]
            b = "{0:b}".format(int(operand))
            binary = BitArray(bin=operand)

            if opcode == "000":
                binary = content[w]
            if opcode == "100":
                memory = -binary.uint
            if opcode == "110":
                memory = binary
            if opcode == "001":
                memory - binary.uint
            if opcode == "011":
                break
            if opcode == "111":
                memory * binary.uint
            if opcode == "101":
                memory / binary.uint
            if opcode == "010":
                memory + binary.uint
            for i in range(len(content)):
                print content[i]
            print "\n"
        break
            