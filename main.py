import csv
import propertyMiner
import getpass
import sys
import interface
import tkinter as tk
from tkinter import simpledialog

jurisdiction, inputFile, outputFile = interface.inputWindow()

username = getpass.getuser() # fetch username

with open(inputFile, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    with open(outputFile, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        header = ['Pin', 'Owner', 'Owner Address', 'Property Address']
        writer.writerow(header) # write the header

        for i in data:
            if jurisdiction == 'Prince William County':
                pin, own, own_add, prop_add = propertyMiner.minerPrinceWilliam(i) #initiate the miner function
                row = (pin, own, own_add, prop_add)

                writer.writerow(row) # write the multiple lines of data

            elif jurisdiction == 'Fairfax County':
                tk.messagebox.showwarning(title="Error", message="Dumbass...under construction")
                sys.exit()

            elif jurisdiction == 'Loudoun County':
                tk.messagebox.showwarning(title="Error", message="Dumbass...under construction")
                sys.exit()
