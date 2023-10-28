import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("900x490")
root.resizable(False,False)

PRIMARY_COLOR ="#212121"
SECONDARY_COLOR ="#1DA756"
PRIM_SHADE1 ="#303030"
SCNDY_SHADE1 ="#136C38"

def getFont(size = 9, bold= False) :
    return("TKDefaultFont", size, "bold" if bold else "normal")
def validate(P):
    empty = P == ""
    digit = empty or P[-1].isdigit
    minus = P=="-" and len(P) == 1
    decimal = P.count(".") == 1
    out =empty or digit or minus or decimal
    return out
calcFunc ={
    "cf": lambda x:x *9/5+32,
    "ck": lambda x:x +273.15,
    "fc": lambda x:(x-32)*5/9,
    "kc": lambda x:x-273.15,
}

calcFunc["fk"] = lambda x:calcFunc["ck"](calcFunc["fc"](x))
calcFunc["kf"] = lambda x:calcFunc["cf"](calcFunc["kc"](x))


def convert(fromInpt, fromUnitVar, toUnitVar, resultVar):
    fromU = fromUnitVar.get().lower()
    toU = toUnitVar.get()[0].lower()
    
    try:
        val = float(fromInpt.get())
    except ValueError:
        resultVar.set("Error!")
        return
    
    if fromU == toU:
        res = val
    else:
        res = calcFunc[fromU + toU](val)
        
    if not toU =="k":
        resultVar.set(f"{res:2f}°{toU.upper()}")
    else:
        resultVar.set(f"{res:2f} {toU.upper()}")
        
reg = root.register(validate)
borderFrame = tk.Frame(root, bg=SECONDARY_COLOR, width=450, height=510)
borderFrame.place(x=0, y=0)

leftFrame = tk.Frame(borderFrame, bg=PRIMARY_COLOR, width=440, height=500)
leftFrame.place(x=5, y=5)

enterLabel = tk.Label(leftFrame, text="Enter Temperature", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=getFont(16,True))
enterLabel.place(x=30, y=50)

degLabel = tk.Label(leftFrame, text="Degree", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=getFont(9))
degLabel.place(x=30, y=120)

inptEntry = tk.Entry(leftFrame, bg=PRIM_SHADE1, fg="#ffffff", insertbackground="#ffffff", borderwidth=5, relief="flat",validatecommand=(reg,"%P"), validate="key")
inptEntry.place(x=30, y=160, width=265, height=42)

unitVar = tk.StringVar(root)
unitVar.set("C")

convertVar = tk.StringVar(root)
convertVar.set("Farenheit")

s = ttk.Style()
s.configure("unit.TMenubutton", background=SECONDARY_COLOR)
s.configure("unit.TMenubutton", relief="flat")

s.configure("convertTo.Tmenubutton", relief="flat")
s.configure("convertTo.Tmenubutton", background=PRIM_SHADE1)
s.configure("convertTo.Tmenubutton", foreground="#ffffff")
s.configure("convertTo.Tmenubutton", width=320)

unitMenu = ttk.OptionMenu(leftFrame, unitVar, "C", "C", "F", "K", style="unit.TMenubutton")
unitMenu.place(x=300, y=160, width=50, height=42)

convertLabel = tk.Label(leftFrame, text="Convert To", bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=getFont(9))
convertLabel.place(x=30, y=80)

convertMenu = ttk.OptionMenu(leftFrame, convertVar, "Fahrenheit", "Celcius", "Fahrenheit", "Kelvin", style="convertTo.TMenubutton")
convertMenu.place(x=30, y=320, width=320, height=42)

convertButton = tk.Button(leftFrame, text="Convert", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=getFont(12), relief="flat", activebackground=SCNDY_SHADE1, bd=0)
convertButton.place(x=150, y=420, width=140, height=40)

rightFrame = tk.Frame(root, bg=SECONDARY_COLOR, width=450, height=510)
rightFrame.place(x=449, y=2)

resultVar = tk.StringVar(root)
resultVar.set("")

resultLabel = tk.Label(rightFrame, textvariable= resultVar, bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, font=getFont(50, True))
resultLabel.place(relx = 0.5, rely= 0.4901, anchor=tk.CENTER)

convertButton.configure(command = lambda: convert(inptEntry, unitVar, convertVar, resultVar))

root.mainloop()
