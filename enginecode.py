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
        #append so that everything is looped and written
        writeit = open(outputfile, "a")
        #if statements that checks for the opcodes
        if s[:3] == "000":
            s = "JMP "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "100":
            s = "LDN "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "110":
            s = "STO "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "001":
            s = "SUB "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "011":
            s = "STP "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "111":
            s = "MUL "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "101":
            s = "DIV "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
            writeit.writelines(l)

        if s[:3] == "010":
            s = "ADD "
            l = "\n"
            writeit.write(s)
            writeit.writelines(str(int(r, 2)))
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

#actual engine to run the code
def engine(inputfile):
    with open(inputfile) as l:
        content = l.readlines()

    content = [x.strip() for x in content]
    print content
    memory = 0
    cnt = 0
    while True:
        while cnt != len(content):
            r = content[cnt]
            opcode = r[:3]
            operand = r[3:]
            b = "{0:b}".format(int(operand))
            m = "{0:b}".format(memory)
            #print int(r[3:], 2)
            if opcode == "000":#Jumps to a memory address
                cnt = int(operand, 2)-1
            if opcode == "100":#puts the memory in the operand
                r = opcode + m.zfill(len(operand))
                content[cnt] = r
            if opcode == "110":#puts the operand in memory
                memory = int(operand, 2)
            if opcode == "001":#subtracts from accumulator
                c = "{0:b}".format(memory - int(operand, 2))
                r = opcode + str(c)
                content[cnt] = r
            if opcode == "011":#stops execution
                break
            if opcode == "111":#adds from accumulator
                c = "{0:b}".format(memory * int(operand, 2))
                r = opcode + str(c)
                content[cnt] = r
            if opcode == "101":#divides from accumulator
                c = "{0:b}".format(memory / int(operand, 2))
                r = opcode + str(c)
                content[cnt] = r
            if opcode == "010":#adds from accumulator
                c = "{0:b}".format(memory + int(operand, 2))
                r = opcode + str(c)
                content[cnt] = r
            if opcode != "000":
                cnt += 1
        for jesus, count in enumerate(content):
            operand = content[jesus]
            print int(operand[3:], 2)
        break