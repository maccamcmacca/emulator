from bitstring import BitArray 

with open("test.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


s = content[0]
#print s[:3]

readit = open("testassem.txt","r")
for line in readit:
    print line
    r = s[3:]
    print r
    b = BitArray(bin=r)
    print b.uint
    e = b.uint

writeit = open("testassem.txt", "w")
if s[:3] == "011":
    s = "JMP "
    l = "\n"
    writeit.writelines(s)
    writeit.writelines(str(b.uint))
    writeit.writelines(l)
