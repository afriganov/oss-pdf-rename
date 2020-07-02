import pdftotext
import glob
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
direktori = filedialog.askdirectory()
fileList = glob.glob(direktori+"/bzp_izvadak_oss*.pdf")
zklista = []
for x in range(0,len(fileList)):
    with open(fileList[x], "rb") as f:
        pdf = pdftotext.PDF(f)
        f.close()
        a = pdf[0][pdf[0].find("Broj ZK uloška: ")+16:pdf[0].find("Broj zadnjeg dnevnika")].strip()
        zklista.append(a)
        i = zklista.count(a)
        if i>1:
            os.rename(fileList[x],fileList[x].split("\\")[0]+"\\ZK-" + a + "(" +str(i)+ ")" + ".pdf")
        else:
            os.rename(fileList[x], fileList[x].split("\\")[0] + "\\ZK-" +a+".pdf")


fileList = glob.glob(direktori+"/prijepis_posjedovnog_lista*.pdf")
pllista = []
for x in range(0,len(fileList)):
    with open(fileList[x], "rb") as f:
        pdf = pdftotext.PDF(f)
        f.close()
        a = pdf[0][pdf[0].find("Posjedovni list: ")+17:pdf[0].find("Udio")].strip()
        pllista.append(a)
        i = pllista.count(a)
        if i>1:
            os.rename(fileList[x],fileList[x].split("\\")[0]+"\\PL-"+a+" (" +str(i)+ ")" + ".pdf")
        else:
            os.rename(fileList[x], fileList[x].split("\\")[0] + "\\PL-" + a + ".pdf")
