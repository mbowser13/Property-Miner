from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

def inputWindow():

    window = Tk()
    window.title("Property Miner Application")
    selected = StringVar()

    rad1 = Radiobutton(window,text='Prince William County', value='Prince William County', variable=selected)
    rad2 = Radiobutton(window,text='Fairfax County', value='Fairfax County', variable=selected)
    rad3 = Radiobutton(window,text='Loudoun County', value='Loudoun County', variable=selected)

    def clicked():
       return selected.get()

    def browseInputFile():
        inputFilename = filedialog.askopenfilename(initialdir = "/",title = "Select the Input File",filetypes = (("CSV Files","*.csv"),))
        # Change label contents
        return inputFilename

    def browseOutputFile():
        outputFilename = filedialog.askopenfilename(initialdir = "/",title = "Select the Output File",filetypes = (("CSV Files","*.csv"),))
        # Change label contents
        return outputFilename

    btn = Button(window, text="Start Mining", command=window.destroy)

    rad1.grid(column=0, row=0, pady=10, sticky="w")
    rad2.grid(column=0, row=1, pady=10, sticky="w")
    rad3.grid(column=0, row=2, pady=10, sticky="w")
    btn.grid(column=1, row=0, pady=10, padx=30)

    window.mainloop()

    return clicked(), browseInputFile(), browseOutputFile()
