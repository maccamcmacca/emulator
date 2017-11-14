thefile = open("test.txt", "r")
for line in thefile:
    print line,
thefile = open("testassem.txt", "w")
x = raw_input("Enter shit: ")
thefile.write(x)
thefile = open("testassem.txt", "r")
for line in thefile:
    print line,