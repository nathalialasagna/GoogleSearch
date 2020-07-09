from package import GuiGoogle 
#from tkinter import *


if __name__ == "__main__":
    root = GuiGoogle.Tk()
    my_gui = GuiGoogle.GoogleSearchInterface(root)
    root.title('Google Search')
    root.mainloop()