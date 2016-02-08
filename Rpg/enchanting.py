import Tkinter
from collections import OrderedDict

master = Tkinter.Tk()
lbEffect = Tkinter.Listbox(master, height=13, exportselection=False)
lbEffect.grid(row=1, column=0, sticky=Tkinter.N)
lbTarget = Tkinter.Listbox(master, height=2, exportselection=False)
lbTarget.grid(row=1, column=1, sticky=Tkinter.N)
lbMagnitude = Tkinter.Listbox(master, height=10, exportselection=False)
lbMagnitude.grid(row=1, column=2, sticky=Tkinter.N)
lbCharges = Tkinter.Listbox(master, height=6, exportselection=False)
lbCharges.grid(row=1, column=3, sticky=Tkinter.N)
lbDuration = Tkinter.Listbox(master, height=7, exportselection=False)
lbDuration.grid(row=1, column=4, sticky=Tkinter.N)
Total = Tkinter.Text(master, width=5, height=1)
Total.grid(row=2, column=4, sticky=Tkinter.N)
Tkinter.Label(master, text='Effect').grid(row=0, column=0)
Tkinter.Label(master, text='Target').grid(row=0, column=1)
Tkinter.Label(master, text='Magnitude').grid(row=0, column=2)
Tkinter.Label(master, text='Charges').grid(row=0, column=3)
Tkinter.Label(master, text='Duration').grid(row=0, column=4)

def funcReset():
    global Eff, Mag, Char, Tar, Dur
    Eff = 0
    Mag = 0
    Char = 0
    Tar = 0
    Dur = 0

resetButton = Tkinter.Button(master, text="Reset", command=funcReset)
resetButton.grid(row=2, column=2)

Eff = 0
Mag = 0
Char = 0
Tar = 0
Dur = 0
toValue = 0

dEffect = OrderedDict([('Damage: 10', 10), ('Heal: 5', 5), ('Drain Life: 15', 15), ('AC: 20', 20), ('Energy Resistance: 10', 10), ('Enhance Ability: 15', 15), ('Frighten: 20', 20), ('Light: 5', 5), ('Sense Magic: 10', 10), ('Sense Hidden: 20', 20), ('Dispel: 60', 60), ('Invisibility: 50', 50), ('Paralyze: 100', 100)])
dMagnitudeDie = OrderedDict([('1: x1', 1), ('2: x2', 2), ('1d4: x3', 3), ('1d6: x4', 4), ('1d8: x5', 5), ('1d10: x6', 6), ('2d4: x7', 7), ('1d10: x8', 8), ('1d12: x9', 9)])
dMagnitudeNum = OrderedDict([('1: x1', 1), ('2: x2', 2), ('3: x3', 3), ('4: x4', 4), ('5: x5', 5), ('6: x6', 6), ('7: 7x', 7), ('8: 8x', 8), ('9: 9x', 9), ('10: 10x', 10)])
dCharges = OrderedDict([('2: 0', 0), ('5: 5', 5), ('10: 10', 10), ('20: 20', 20), ('30: 30', 30), ('Permanent: 50', 50)])
dTarget = OrderedDict([('Self: 0', 0), ('Touch: 5', 5)])
dDuration = OrderedDict([('Instant: 0', 0), ('1 turn: 5', 5), ('2 turns: 10', 10), ('3 turns: 15', 15), ('4 turns: 20', 20), ('5 turns: 30', 30), ('1 scene: 40', 40), ('Permanent: 0', 0), ('none', 0)])

for kEf, vEf in dEffect.items():
    lbEffect.insert(Tkinter.END, kEf)

#Choose an Effect and make changes to listboxes to support that choice. And return the values.
def EffectSel(x):
    global toValue
    global Eff
    global Mag
    global Char
    global Dur
    global Tar
    global selEfCheck
    selEfCheck = lbEffect.curselection()
    selEf = lbEffect.get(lbEffect.curselection())
    Eff = dEffect[selEf]
    toValue = 0
#Value Calculation
    if selEfCheck < (6,):
        toValue = (Eff * Mag) + Dur + Char + Tar
    else:
        toValue = Eff + Dur + Char + Tar
    Total.delete(1.0, Tkinter.END)
    Total.insert(Tkinter.END, toValue)
#Delete Lisboxes
    lbDuration.delete(0, Tkinter.END)
    lbCharges.delete(0, Tkinter.END)
    lbTarget.delete(0, Tkinter.END)
#Determine Target
    if selEfCheck == (3,) or selEfCheck == (4,) or selEfCheck == (5,) or selEfCheck == (7,) or selEfCheck == (8,) or selEfCheck == (9,) or selEfCheck == (11,):
        lbTarget.insert(Tkinter.END, 'Self: 0')
    elif selEfCheck == (0,) or selEfCheck == (2,) or selEfCheck == (6,) or selEfCheck == (12,):
        lbTarget.insert(Tkinter.END, 'Touch: 5')
    else:
        for kTa in dTarget:
            lbTarget.insert(Tkinter.END, kTa)
#Determine Magnitude and Charges
    if selEfCheck < (6,):
        lbMagnitude.delete(0, Tkinter.END)
        if selEfCheck < (3,):
            lbDuration.delete(0, Tkinter.END)
            for kDie in dMagnitudeDie:
                lbMagnitude.insert(Tkinter.END, kDie)
            for kCh in dCharges:
                lbCharges.insert(Tkinter.END, kCh)
        else:
            lbDuration.delete(0, Tkinter.END)
            for kCh in dCharges:
                lbCharges.insert(Tkinter.END, kCh)
            for kMag in dMagnitudeNum:
                lbMagnitude.insert(Tkinter.END, kMag)
    else:
        lbMagnitude.delete(0, Tkinter.END)
        for kCh in dCharges:
            lbCharges.insert(Tkinter.END, kCh)

#Choose Target and return value.
def TargetSel(x):
    global toValue
    global Eff
    global Mag
    global Char
    global Dur
    global Tar
    selTar = lbTarget.get(lbTarget.curselection())
    if selTar == 'Touch: 5':
        Tar = 5
    elif selTar == 'Self: 0':
        Tar = 0
    Tar = dTarget[selTar]
    toValue = 0
#Value Calculation
    if selEfCheck < (6,):
        toValue = (Eff * Mag) + Dur + Char + Tar
    else:
        toValue = Eff + Dur + Char + Tar
    Total.delete(1.0, Tkinter.END)
    Total.insert(Tkinter.END, toValue)

#Choose Charges and return values. Also if Charge permanent, make the Duration Permanent.
def ChargesSel(x):
    global toValue
    global Eff
    global Mag
    global Char
    global Dur
    global Tar
    selCh = lbCharges.get(lbCharges.curselection())
    Char = dCharges[selCh]
    toValue = 0
    #Value Calculation
    if selEfCheck < (6,):
        toValue = (Eff * Mag) + Dur + Char + Tar
    else:
        toValue = Eff + Dur + Char + Tar
    lbDuration.delete(0, Tkinter.END)
#check if Permanent Charges has been selected and sets Duration accordingly.
    if selEfCheck == (0,) or selEfCheck == (1,) or selEfCheck == (2,) or selEfCheck == (10,):
        lbDuration.insert(Tkinter.END, 'none')
    elif selEfCheck == (6,) or selEfCheck == (9,) or selEfCheck == (11,) or selEfCheck == (12,):
        for kDur in dDuration:
            if kDur != 'Permanent: 0' and kDur != 'none':
                lbDuration.insert(Tkinter.END, kDur)
    else:
        for kDur in dDuration:
            if kDur != 'Permanent: 0' and kDur != 'none':
                lbDuration.insert(Tkinter.END, kDur)
        if selCh == 'Permanent: 50':
            lbDuration.delete(0, Tkinter.END)
            lbDuration.insert(Tkinter.END, 'Permanent: 0')

    Total.delete(1.0, Tkinter.END)
    Total.insert(Tkinter.END, toValue)

#Choose Magnitude and return value. Also Check what Dictionary the Magnitude is.
def MagnitudeSel(x):
    global toValue
    global Eff
    global Mag
    global Char
    global Dur
    global Tar
    selMag = lbMagnitude.get(lbMagnitude.curselection())
    MagCheck = lbMagnitude.get(Tkinter.END)
    if MagCheck == '1d12: x9':
        Mag = dMagnitudeDie[selMag]
    else:
        Mag = dMagnitudeNum[selMag]
    toValue = 0
#Value Calculation
    if selEfCheck < (6,):
        toValue = (Eff * Mag) + Dur + Char + Tar
    else:
        toValue = Eff + Dur + Char + Tar
    Total.delete(1.0, Tkinter.END)
    Total.insert(Tkinter.END, toValue)
#Choose Duration, automatically set as Permanent if Charges Permanent. Return values.
def DurationSel(x):
    global toValue
    global Eff
    global Mag
    global Char
    global Dur
    global Tar
    selDur = lbDuration.get(lbDuration.curselection())
    Dur = dDuration[selDur]
    toValue = 0
#Value Calculation
    if selEfCheck < (6,):
        toValue = (Eff * Mag) + Dur + Char + Tar
    else:
        toValue = Eff + Dur + Char + Tar
    Total.delete(1.0, Tkinter.END)
    Total.insert(Tkinter.END, toValue)
#pack and run everything
Total.insert(Tkinter.END, toValue)
lbEffect.bind('<<ListboxSelect>>', EffectSel)
lbTarget.bind('<<ListboxSelect>>', TargetSel)
lbMagnitude.bind('<<ListboxSelect>>', MagnitudeSel)
lbCharges.bind('<<ListboxSelect>>', ChargesSel)
lbDuration.bind('<<ListboxSelect>>', DurationSel)
Tkinter.mainloop()