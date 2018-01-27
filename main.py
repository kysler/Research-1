import glob
import subprocess as sp
import tkinter as tk
import cosineSim as cs
from cosineSim import cosineSim
from tkinter import filedialog


#Function to call Cosine Similarity to gather results.
def similar(a, b):
    return cosineSim(a, b)*100

#Temporary display of Results with notepad
def openPad():
    programName = "notepad.exe"
    fileName = "result.txt"
    sp.Popen([programName, fileName])

def openFileDialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Alyas Vince\\PycharmProjects\\doit\\venv\\database")
    return file_path

result = open('result.txt', "w")
result.writelines("")
result.close

with open (openFileDialog(), "r") as myfile:
    data=myfile.readlines()

counter = 0
for filename in glob.glob("database/*.txt"):
    with open(filename, 'r') as fd:
        data2 = fd.readlines()
        counter += 1

    ratio = round(similar(data, data2), 2)

    resultText = "\n" + filename + "\nResults\n" + counter.__str__() + " || " + ratio.__str__()+"%" + "\n ---------- \n"

    if(ratio >= 30):
        result = open('result.txt', "a+")
        result.writelines(resultText)
        result.close

openPad()


