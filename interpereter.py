from bitstring import BitArray 
import interperitercode

interperitercode.wipe("testassem.txt")
interperitercode.disassemble("test.txt", "testassem.txt")
interperitercode.assemble("testassem.txt", "testass.txt")