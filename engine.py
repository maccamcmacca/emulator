import enginecode
from Tkinter import Tk
from tkFileDialog import askopenfilename

#Tk().withdraw()
filename = askopenfilename()

enginecode.engine(str(filename))