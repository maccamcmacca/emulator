# The Macca Emulator
#v1.0.0

Basically an emulator of an 8 bit computer.

Instruction set similiar to the SSEM

Instruction Set:

000 = JMP Jumps to an address  

100 = LDN Loads the address in the memory to the current address

110 = STO Stores the address in the memory to the accumulator

001 = SUB Makes the accumulator = accumulator - opcode

011 = STP Stops the program

111 = MUL Multiplies the accumulator = accumulator * opcode

101 = DIV Multiplies the accumulator = accumulator / opcode

010 = ADD Multiplies the accumulator = accumulator + opcode
