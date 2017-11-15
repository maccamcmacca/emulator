from bitstring import BitArray 

def disassemble(inputfile, outputfile):
    with open(inputfile) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]


    for w in range(len(content)):
        
        s = content[w]
        
        readit = open(inputfile, "r")
        for line in readit:
            r = s[3:]
            b = BitArray(bin=r)

        writeit = open(outputfile, "a")
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

def assemble(inputfile, outputfile):
    with open(inputfile) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip(" ") for x in content]

    for w in range(len(content)):
        
        s = content[w]
        r = int(s[3:])
        b = "{0:b}".format(r)
        
        writeit = open(outputfile, "a")
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

        writeit.write(str(b).zfill(5))
        writeit.write("\n")


def wipe(inputfile):
    s = open(inputfile, "w")
    s.writelines("")