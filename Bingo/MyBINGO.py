import random
from tkinter import *


def generate_c1B():
    listC1B = []
    while (len(listC1B) <=4):
        b = random.choice(range(1,15))
        if b not in listC1B:
            listC1B.append(b)
    return listC1B
def generate_c1I():
    listC1I = []
    while (len(listC1I) <=4):
        i = random.choice(range(16,30))
        if i not in listC1I:
            listC1I.append(i)
    return listC1I
def generate_c1N():
    listC1N = []
    while (len(listC1N) <=3):
        n = random.choice(range(31,45))
        if n not in listC1N:
            listC1N.append(n)
    return listC1N
def generate_c1G():
    listC1G = []
    while (len(listC1G) <=4):
        g = random.choice(range(46,60))
        if g not in listC1G:
            listC1G.append(g)
    return listC1G
def generate_c1O():
    listC1O = []
    while (len(listC1O) <=4):
        o = random.choice(range(61,75))
        if o not in listC1O:
            listC1O.append(o)
    return listC1O

def generate_c2B():
    listC2B = []
    while (len(listC2B) <=4):
        b = random.choice(range(1,15))
        if b not in listC2B:
            listC2B.append(b)
    return listC2B
def generate_c2I():
    listC2I = []
    while (len(listC2I) <=4):
        i = random.choice(range(16,30))
        if i not in listC2I:
            listC2I.append(i)
    return listC2I
def generate_c2N():
    listC2N = []
    while (len(listC2N) <=3):
        n = random.choice(range(31,45))
        if n not in listC2N:
            listC2N.append(n)
    return listC2N
def generate_c2G():
    listC2G = []
    while (len(listC2G) <=4):
        g = random.choice(range(46,60))
        if g not in listC2G:
            listC2G.append(g)
    return listC2G
def generate_c2O():
    listC2O = []
    while (len(listC2O) <=4):
        o = random.choice(range(61,75))
        if o not in listC2O:
            listC2O.append(o)
    return listC2O

def generate_c3B():
    listC3B = []
    while (len(listC3B) <=4):
        b = random.choice(range(1,15))
        if b not in listC3B:
            listC3B.append(b)
    return listC3B
def generate_c3I():
    listC3I = []
    while (len(listC3I) <=4):
        i = random.choice(range(16,30))
        if i not in listC3I:
            listC3I.append(i)
    return listC3I
def generate_c3N():
    listC3N = []
    while (len(listC3N) <=3):
        n = random.choice(range(31,45))
        if n not in listC3N:
            listC3N.append(n)
    return listC3N
def generate_c3G():
    listC3G = []
    while (len(listC3G) <=4):
        g = random.choice(range(46,60))
        if g not in listC3G:
            listC3G.append(g)
    return listC3G
def generate_c3O():
    listC3O = []
    while (len(listC3O) <=4):
        o = random.choice(range(61,75))
        if o not in listC3O:
            listC3O.append(o)
    return listC3O

def generate_c4B():
    listC4B = []
    while (len(listC4B) <=4):
        b = random.choice(range(1,15))
        if b not in listC4B:
            listC4B.append(b)
    return listC4B
def generate_c4I():
    listC4I = []
    while (len(listC4I) <=4):
        i = random.choice(range(16,30))
        if i not in listC4I:
            listC4I.append(i)
    return listC4I
def generate_c4N():
    listC4N = []
    while (len(listC4N) <=3):
        n = random.choice(range(31,45))
        if n not in listC4N:
            listC4N.append(n)
    return listC4N
def generate_c4G():
    listC4G = []
    while (len(listC4G) <=4):
        g = random.choice(range(46,60))
        if g not in listC4G:
            listC4G.append(g)
    return listC4G
def generate_c4O():
    listC4O = []
    while (len(listC4O) <=4):
        o = random.choice(range(61,75))
        if o not in listC4O:
            listC4O.append(o)
    return listC4O

def enter_is_match(event):
    k = NumberEntry.get()
    NumberEntry.delete(0,"end")
    NumberEntry.insert(0,"")
    num_listo2.config(text = str(num_listo2["text"]) + "\n" + k)
    if str(c1B1["text"]) == k:
        c1B1.config(bg='green')
    if str(c1B2["text"]) == k:
        c1B2.config(bg='green')
    if str(c1B3["text"]) == k:
        c1B3.config(bg='green')
    if str(c1B4["text"]) == k:
        c1B4.config(bg='green')
    if str(c1B5["text"]) == k:
        c1B5.config(bg='green')
    if str(c1I1["text"]) == k:
        c1I1.config(bg='green')
    if str(c1I2["text"]) == k:
        c1I2.config(bg='green')
    if str(c1I3["text"]) == k:
        c1I3.config(bg='green')
    if str(c1I4["text"]) == k:
        c1I4.config(bg='green')
    if str(c1I5["text"]) == k:
        c1I5.config(bg='green')
    if str(c1N1["text"]) == k:
        c1N1.config(bg='green')
    if str(c1N2["text"]) == k:
        c1N2.config(bg='green')
    if str(c1N4["text"]) == k:
        c1N4.config(bg='green')
    if str(c1N5["text"]) == k:
        c1N5.config(bg='green')
    if str(c1G1["text"]) == k:
        c1G1.config(bg='green')
    if str(c1G2["text"]) == k:
        c1G2.config(bg='green')
    if str(c1G3["text"]) == k:
        c1G3.config(bg='green')
    if str(c1G4["text"]) == k:
        c1G4.config(bg='green')
    if str(c1G5["text"]) == k:
        c1G5.config(bg='green')
    if str(c1O1["text"]) == k:
        c1O1.config(bg='green')
    if str(c1O2["text"]) == k:
        c1O2.config(bg='green')
    if str(c1O3["text"]) == k:
        c1O3.config(bg='green')
    if str(c1O4["text"]) == k:
        c1O4.config(bg='green')
    if str(c1O5["text"]) == k:
        c1O5.config(bg='green')
    if str(c2B1["text"]) == k:
        c2B1.config(bg='green')
    if str(c2B2["text"]) == k:
        c2B2.config(bg='green')
    if str(c2B3["text"]) == k:
        c2B3.config(bg='green')
    if str(c2B4["text"]) == k:
        c2B4.config(bg='green')
    if str(c2B5["text"]) == k:
        c2B5.config(bg='green')
    if str(c2I1["text"]) == k:
        c2I1.config(bg='green')
    if str(c2I2["text"]) == k:
        c2I2.config(bg='green')
    if str(c2I3["text"]) == k:
        c2I3.config(bg='green')
    if str(c2I4["text"]) == k:
        c2I4.config(bg='green')
    if str(c2I5["text"]) == k:
        c2I5.config(bg='green')
    if str(c2N1["text"]) == k:
        c2N1.config(bg='green')
    if str(c2N2["text"]) == k:
        c2N2.config(bg='green')
    if str(c2N4["text"]) == k:
        c2N4.config(bg='green')
    if str(c2N5["text"]) == k:
        c2N5.config(bg='green')
    if str(c2G1["text"]) == k:
        c2G1.config(bg='green')
    if str(c2G2["text"]) == k:
        c2G2.config(bg='green')
    if str(c2G3["text"]) == k:
        c2G3.config(bg='green')
    if str(c2G4["text"]) == k:
        c2G4.config(bg='green')
    if str(c2G5["text"]) == k:
        c2G5.config(bg='green')
    if str(c2O1["text"]) == k:
        c2O1.config(bg='green')
    if str(c2O2["text"]) == k:
        c2O2.config(bg='green')
    if str(c2O3["text"]) == k:
        c2O3.config(bg='green')
    if str(c2O4["text"]) == k:
        c2O4.config(bg='green')
    if str(c2O5["text"]) == k:
        c2O5.config(bg='green')
    if str(c3B1["text"]) == k:
        c3B1.config(bg='green')
    if str(c3B2["text"]) == k:
        c3B2.config(bg='green')
    if str(c3B3["text"]) == k:
        c3B3.config(bg='green')
    if str(c3B4["text"]) == k:
        c3B4.config(bg='green')
    if str(c3B5["text"]) == k:
        c3B5.config(bg='green')
    if str(c3I1["text"]) == k:
        c3I1.config(bg='green')
    if str(c3I2["text"]) == k:
        c3I2.config(bg='green')
    if str(c3I3["text"]) == k:
        c3I3.config(bg='green')
    if str(c3I4["text"]) == k:
        c3I4.config(bg='green')
    if str(c3I5["text"]) == k:
        c3I5.config(bg='green')
    if str(c3N1["text"]) == k:
        c3N1.config(bg='green')
    if str(c3N2["text"]) == k:
        c3N2.config(bg='green')
    if str(c3N4["text"]) == k:
        c3N4.config(bg='green')
    if str(c3N5["text"]) == k:
        c3N5.config(bg='green')
    if str(c3G1["text"]) == k:
        c3G1.config(bg='green')
    if str(c3G2["text"]) == k:
        c3G2.config(bg='green')
    if str(c3G3["text"]) == k:
        c3G3.config(bg='green')
    if str(c3G4["text"]) == k:
        c3G4.config(bg='green')
    if str(c3G5["text"]) == k:
        c3G5.config(bg='green')
    if str(c3O1["text"]) == k:
        c3O1.config(bg='green')
    if str(c3O2["text"]) == k:
        c3O2.config(bg='green')
    if str(c3O3["text"]) == k:
        c3O3.config(bg='green')
    if str(c3O4["text"]) == k:
        c3O4.config(bg='green')
    if str(c3O5["text"]) == k:
        c3O5.config(bg='green')
    if str(c4B1["text"]) == k:
        c4B1.config(bg='green')
    if str(c4B2["text"]) == k:
        c4B2.config(bg='green')
    if str(c4B3["text"]) == k:
        c4B3.config(bg='green')
    if str(c4B4["text"]) == k:
        c4B4.config(bg='green')
    if str(c4B5["text"]) == k:
        c4B5.config(bg='green')
    if str(c4I1["text"]) == k:
        c4I1.config(bg='green')
    if str(c4I2["text"]) == k:
        c4I2.config(bg='green')
    if str(c4I3["text"]) == k:
        c4I3.config(bg='green')
    if str(c4I4["text"]) == k:
        c4I4.config(bg='green')
    if str(c4I5["text"]) == k:
        c4I5.config(bg='green')
    if str(c4N1["text"]) == k:
        c4N1.config(bg='green')
    if str(c4N2["text"]) == k:
        c4N2.config(bg='green')
    if str(c4N4["text"]) == k:
        c4N4.config(bg='green')
    if str(c4N5["text"]) == k:
        c4N5.config(bg='green')
    if str(c4G1["text"]) == k:
        c4G1.config(bg='green')
    if str(c4G2["text"]) == k:
        c4G2.config(bg='green')
    if str(c4G3["text"]) == k:
        c4G3.config(bg='green')
    if str(c4G4["text"]) == k:
        c4G4.config(bg='green')
    if str(c4G5["text"]) == k:
        c4G5.config(bg='green')
    if str(c4O1["text"]) == k:
        c4O1.config(bg='green')
    if str(c4O2["text"]) == k:
        c4O2.config(bg='green')
    if str(c4O3["text"]) == k:
        c4O3.config(bg='green')
    if str(c4O4["text"]) == k:
        c4O4.config(bg='green')
    if str(c4O5["text"]) == k:
        c4O5.config(bg='green')

    #Win Check
    '''Check for win with Horizontal'''
    #Card1
    if chkhorizontal.get() == 1:
        if c1B1.cget("bg") =='green' and c1I1.cget("bg") =='green' and c1N1.cget("bg") =='green' and c1G1.cget("bg") =='green' and c1O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B2.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1N2.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B3.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G3.cget("bg") =='green' and c1O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B4.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B5.cget("bg") =='green' and c1I5.cget("bg") =='green' and c1N5.cget("bg") =='green' and c1G5.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2I1.cget("bg") =='green' and c2N1.cget("bg") =='green' and c2G1.cget("bg") =='green' and c2O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B2.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2N2.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2O2.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B3.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G3.cget("bg") =='green' and c2O3.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B4.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2O4.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B5.cget("bg") =='green' and c2I5.cget("bg") =='green' and c2N5.cget("bg") =='green' and c2G5.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3I1.cget("bg") =='green' and c3N1.cget("bg") =='green' and c3G1.cget("bg") =='green' and c3O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B2.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3N2.cget("bg") =='green' and c3G2.cget("bg") =='green' and c3O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B3.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3G3.cget("bg") =='green' and c3O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B4.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B5.cget("bg") =='green' and c3I5.cget("bg") =='green' and c3N5.cget("bg") =='green' and c3G5.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4I1.cget("bg") =='green' and c4N1.cget("bg") =='green' and c4G1.cget("bg") =='green' and c4O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B2.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4N2.cget("bg") =='green' and c4G2.cget("bg") =='green' and c4O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B3.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4G3.cget("bg") =='green' and c4O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B4.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B5.cget("bg") =='green' and c4I5.cget("bg") =='green' and c4N5.cget("bg") =='green' and c4G5.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)


    '''Check for win with vertical'''
    if chkvertical.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1B2.cget("bg") =='green' and c1B3.cget("bg") =='green' and c1B4.cget("bg") =='green' and c1B5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1I1.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1I5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1N1.cget("bg") =='green' and c1N2.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1N5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1G1.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1G3.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1O1.cget("bg") =='green' and c1O2.cget("bg") =='green' and c1O3.cget("bg") =='green' and c1O4.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2B2.cget("bg") =='green' and c2B3.cget("bg") =='green' and c2B4.cget("bg") =='green' and c2B5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2I1.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2I5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2N1.cget("bg") =='green' and c2N2.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2N5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2G1.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2G3.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2O1.cget("bg") =='green' and c2O2.cget("bg") =='green' and c2O3.cget("bg") =='green' and c2O4.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3B2.cget("bg") =='green' and c3B3.cget("bg") =='green' and c3B4.cget("bg") =='green' and c3B5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3I1.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3I5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3N1.cget("bg") =='green' and c3N2.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3N5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3G1.cget("bg") =='green' and c3G2.cget("bg") =='green' and c3G3.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3O1.cget("bg") =='green' and c3O2.cget("bg") =='green' and c3O3.cget("bg") =='green' and c3O4.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4B2.cget("bg") =='green' and c4B3.cget("bg") =='green' and c4B4.cget("bg") =='green' and c4B5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4I1.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4I5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4N1.cget("bg") =='green' and c4N2.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4N5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4G1.cget("bg") =='green' and c4G2.cget("bg") =='green' and c4G3.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4O1.cget("bg") =='green' and c4O2.cget("bg") =='green' and c4O3.cget("bg") =='green' and c4O4.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

    '''Check for win with Diagonal'''
    if chkdiagonal.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)
        if c1B5.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)
        if c2B5.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2O1.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") == 'green' and c3I2.cget("bg") == 'green' and c3N3.cget("bg") == 'green' and c3G4.cget("bg") == 'green' and c3O5.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Diagonally on " + cardwon)
        if c3B5.cget("bg") == 'green' and c3I4.cget("bg") == 'green' and c3N3.cget("bg") == 'green' and c3G2.cget("bg") == 'green' and c3O1.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        # Card 4
        if c4B1.cget("bg") == 'green' and c4I2.cget("bg") == 'green' and c4N3.cget("bg") == 'green' and c4G4.cget("bg") == 'green' and c4O5.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Diagonally on " + cardwon)
        if c4B5.cget("bg") == 'green' and c4I4.cget("bg") == 'green' and c4N3.cget("bg") == 'green' and c4G2.cget("bg") == 'green' and c4O1.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)


    '''Check for win with 4 Corners'''
    if chkcorners.get() ==1:
        #Card 1
        if c1B1.cget("bg") == 'green' and c1B5.cget("bg") == 'green' and c1O1.cget("bg") == 'green' and c1O5.cget("bg") == 'green':
            cardwon = 'Card 1!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 2
        if c2B1.cget("bg") == 'green' and c2B5.cget("bg") == 'green' and c2O1.cget("bg") == 'green' and c2O5.cget("bg") == 'green':
            cardwon = 'Card 2!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 3
        if c3B1.cget("bg") == 'green' and c3B5.cget("bg") == 'green' and c3O1.cget("bg") == 'green' and c3O5.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 4
        if c4B1.cget("bg") == 'green' and c4B5.cget("bg") == 'green' and c4O1.cget("bg") == 'green' and c4O5.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

    '''Check for Cover all'''
    if chkcoverall.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1B2.cget("bg") =='green' and c1B3.cget("bg") =='green' and c1B4.cget("bg") =='green' and c1B5.cget("bg") =='green' \
            and c1I2.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1I5.cget("bg") =='green' \
            and c1N3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1N5.cget("bg") =='green' \
            and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G5.cget("bg") =='green' \
            and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2B2.cget("bg") =='green' and c2B3.cget("bg") =='green' and c2B4.cget("bg") =='green' and c2B5.cget("bg") =='green' \
            and c2I2.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2I5.cget("bg") =='green' \
            and c2N3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2N5.cget("bg") =='green' \
            and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G5.cget("bg") =='green' \
            and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3B2.cget("bg") =='green' and c3B3.cget("bg") =='green' and c3B4.cget("bg") =='green' and c3B5.cget("bg") =='green' \
            and c3I2.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3I5.cget("bg") =='green' \
            and c3N3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3N5.cget("bg") =='green' \
            and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G5.cget("bg") =='green' \
            and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4B2.cget("bg") =='green' and c4B3.cget("bg") =='green' and c4B4.cget("bg") =='green' and c4B5.cget("bg") =='green' \
            and c4I2.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4I5.cget("bg") =='green' \
            and c4N3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4N5.cget("bg") =='green' \
            and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G5.cget("bg") =='green' \
            and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

def button_is_match():
    k = NumberEntry.get()
    NumberEntry.delete(0,"end")
    NumberEntry.insert(0,"")
    num_listo2.config(text = str(num_listo2["text"]) + "\n" + k)
    if str(c1B1["text"]) == k:
        c1B1.config(bg='green')
    if str(c1B2["text"]) == k:
        c1B2.config(bg='green')
    if str(c1B3["text"]) == k:
        c1B3.config(bg='green')
    if str(c1B4["text"]) == k:
        c1B4.config(bg='green')
    if str(c1B5["text"]) == k:
        c1B5.config(bg='green')
    if str(c1I1["text"]) == k:
        c1I1.config(bg='green')
    if str(c1I2["text"]) == k:
        c1I2.config(bg='green')
    if str(c1I3["text"]) == k:
        c1I3.config(bg='green')
    if str(c1I4["text"]) == k:
        c1I4.config(bg='green')
    if str(c1I5["text"]) == k:
        c1I5.config(bg='green')
    if str(c1N1["text"]) == k:
        c1N1.config(bg='green')
    if str(c1N2["text"]) == k:
        c1N2.config(bg='green')
    if str(c1N4["text"]) == k:
        c1N4.config(bg='green')
    if str(c1N5["text"]) == k:
        c1N5.config(bg='green')
    if str(c1G1["text"]) == k:
        c1G1.config(bg='green')
    if str(c1G2["text"]) == k:
        c1G2.config(bg='green')
    if str(c1G3["text"]) == k:
        c1G3.config(bg='green')
    if str(c1G4["text"]) == k:
        c1G4.config(bg='green')
    if str(c1G5["text"]) == k:
        c1G5.config(bg='green')
    if str(c1O1["text"]) == k:
        c1O1.config(bg='green')
    if str(c1O2["text"]) == k:
        c1O2.config(bg='green')
    if str(c1O3["text"]) == k:
        c1O3.config(bg='green')
    if str(c1O4["text"]) == k:
        c1O4.config(bg='green')
    if str(c1O5["text"]) == k:
        c1O5.config(bg='green')
    if str(c2B1["text"]) == k:
        c2B1.config(bg='green')
    if str(c2B2["text"]) == k:
        c2B2.config(bg='green')
    if str(c2B3["text"]) == k:
        c2B3.config(bg='green')
    if str(c2B4["text"]) == k:
        c2B4.config(bg='green')
    if str(c2B5["text"]) == k:
        c2B5.config(bg='green')
    if str(c2I1["text"]) == k:
        c2I1.config(bg='green')
    if str(c2I2["text"]) == k:
        c2I2.config(bg='green')
    if str(c2I3["text"]) == k:
        c2I3.config(bg='green')
    if str(c2I4["text"]) == k:
        c2I4.config(bg='green')
    if str(c2I5["text"]) == k:
        c2I5.config(bg='green')
    if str(c2N1["text"]) == k:
        c2N1.config(bg='green')
    if str(c2N2["text"]) == k:
        c2N2.config(bg='green')
    if str(c2N4["text"]) == k:
        c2N4.config(bg='green')
    if str(c2N5["text"]) == k:
        c2N5.config(bg='green')
    if str(c2G1["text"]) == k:
        c2G1.config(bg='green')
    if str(c2G2["text"]) == k:
        c2G2.config(bg='green')
    if str(c2G3["text"]) == k:
        c2G3.config(bg='green')
    if str(c2G4["text"]) == k:
        c2G4.config(bg='green')
    if str(c2G5["text"]) == k:
        c2G5.config(bg='green')
    if str(c2O1["text"]) == k:
        c2O1.config(bg='green')
    if str(c2O2["text"]) == k:
        c2O2.config(bg='green')
    if str(c2O3["text"]) == k:
        c2O3.config(bg='green')
    if str(c2O4["text"]) == k:
        c2O4.config(bg='green')
    if str(c2O5["text"]) == k:
        c2O5.config(bg='green')
    if str(c3B1["text"]) == k:
        c3B1.config(bg='green')
    if str(c3B2["text"]) == k:
        c3B2.config(bg='green')
    if str(c3B3["text"]) == k:
        c3B3.config(bg='green')
    if str(c3B4["text"]) == k:
        c3B4.config(bg='green')
    if str(c3B5["text"]) == k:
        c3B5.config(bg='green')
    if str(c3I1["text"]) == k:
        c3I1.config(bg='green')
    if str(c3I2["text"]) == k:
        c3I2.config(bg='green')
    if str(c3I3["text"]) == k:
        c3I3.config(bg='green')
    if str(c3I4["text"]) == k:
        c3I4.config(bg='green')
    if str(c3I5["text"]) == k:
        c3I5.config(bg='green')
    if str(c3N1["text"]) == k:
        c3N1.config(bg='green')
    if str(c3N2["text"]) == k:
        c3N2.config(bg='green')
    if str(c3N4["text"]) == k:
        c3N4.config(bg='green')
    if str(c3N5["text"]) == k:
        c3N5.config(bg='green')
    if str(c3G1["text"]) == k:
        c3G1.config(bg='green')
    if str(c3G2["text"]) == k:
        c3G2.config(bg='green')
    if str(c3G3["text"]) == k:
        c3G3.config(bg='green')
    if str(c3G4["text"]) == k:
        c3G4.config(bg='green')
    if str(c3G5["text"]) == k:
        c3G5.config(bg='green')
    if str(c3O1["text"]) == k:
        c3O1.config(bg='green')
    if str(c3O2["text"]) == k:
        c3O2.config(bg='green')
    if str(c3O3["text"]) == k:
        c3O3.config(bg='green')
    if str(c3O4["text"]) == k:
        c3O4.config(bg='green')
    if str(c3O5["text"]) == k:
        c3O5.config(bg='green')
    if str(c4B1["text"]) == k:
        c4B1.config(bg='green')
    if str(c4B2["text"]) == k:
        c4B2.config(bg='green')
    if str(c4B3["text"]) == k:
        c4B3.config(bg='green')
    if str(c4B4["text"]) == k:
        c4B4.config(bg='green')
    if str(c4B5["text"]) == k:
        c4B5.config(bg='green')
    if str(c4I1["text"]) == k:
        c4I1.config(bg='green')
    if str(c4I2["text"]) == k:
        c4I2.config(bg='green')
    if str(c4I3["text"]) == k:
        c4I3.config(bg='green')
    if str(c4I4["text"]) == k:
        c4I4.config(bg='green')
    if str(c4I5["text"]) == k:
        c4I5.config(bg='green')
    if str(c4N1["text"]) == k:
        c4N1.config(bg='green')
    if str(c4N2["text"]) == k:
        c4N2.config(bg='green')
    if str(c4N4["text"]) == k:
        c4N4.config(bg='green')
    if str(c4N5["text"]) == k:
        c4N5.config(bg='green')
    if str(c4G1["text"]) == k:
        c4G1.config(bg='green')
    if str(c4G2["text"]) == k:
        c4G2.config(bg='green')
    if str(c4G3["text"]) == k:
        c4G3.config(bg='green')
    if str(c4G4["text"]) == k:
        c4G4.config(bg='green')
    if str(c4G5["text"]) == k:
        c4G5.config(bg='green')
    if str(c4O1["text"]) == k:
        c4O1.config(bg='green')
    if str(c4O2["text"]) == k:
        c4O2.config(bg='green')
    if str(c4O3["text"]) == k:
        c4O3.config(bg='green')
    if str(c4O4["text"]) == k:
        c4O4.config(bg='green')
    if str(c4O5["text"]) == k:
        c4O5.config(bg='green')

    #Win Check
    '''Check for win with Horizontal'''
    #Card1
    if chkhorizontal.get() == 1:
        if c1B1.cget("bg") =='green' and c1I1.cget("bg") =='green' and c1N1.cget("bg") =='green' and c1G1.cget("bg") =='green' and c1O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B2.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1N2.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B3.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G3.cget("bg") =='green' and c1O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B4.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c1B5.cget("bg") =='green' and c1I5.cget("bg") =='green' and c1N5.cget("bg") =='green' and c1G5.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2I1.cget("bg") =='green' and c2N1.cget("bg") =='green' and c2G1.cget("bg") =='green' and c2O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B2.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2N2.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2O2.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B3.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G3.cget("bg") =='green' and c2O3.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B4.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2O4.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c2B5.cget("bg") =='green' and c2I5.cget("bg") =='green' and c2N5.cget("bg") =='green' and c2G5.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3I1.cget("bg") =='green' and c3N1.cget("bg") =='green' and c3G1.cget("bg") =='green' and c3O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B2.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3N2.cget("bg") =='green' and c3G2.cget("bg") =='green' and c3O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B3.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3G3.cget("bg") =='green' and c3O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B4.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c3B5.cget("bg") =='green' and c3I5.cget("bg") =='green' and c3N5.cget("bg") =='green' and c3G5.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4I1.cget("bg") =='green' and c4N1.cget("bg") =='green' and c4G1.cget("bg") =='green' and c4O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B2.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4N2.cget("bg") =='green' and c4G2.cget("bg") =='green' and c4O2.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B3.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4G3.cget("bg") =='green' and c4O3.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B4.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4O4.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)
        if c4B5.cget("bg") =='green' and c4I5.cget("bg") =='green' and c4N5.cget("bg") =='green' and c4G5.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won horizontally on "+ cardwon)


    '''Check for win with vertical'''
    if chkvertical.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1B2.cget("bg") =='green' and c1B3.cget("bg") =='green' and c1B4.cget("bg") =='green' and c1B5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1I1.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1I5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1N1.cget("bg") =='green' and c1N2.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1N5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1G1.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1G3.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c1O1.cget("bg") =='green' and c1O2.cget("bg") =='green' and c1O3.cget("bg") =='green' and c1O4.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2B2.cget("bg") =='green' and c2B3.cget("bg") =='green' and c2B4.cget("bg") =='green' and c2B5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2I1.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2I5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2N1.cget("bg") =='green' and c2N2.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2N5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2G1.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2G3.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c2O1.cget("bg") =='green' and c2O2.cget("bg") =='green' and c2O3.cget("bg") =='green' and c2O4.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3B2.cget("bg") =='green' and c3B3.cget("bg") =='green' and c3B4.cget("bg") =='green' and c3B5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3I1.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3I5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3N1.cget("bg") =='green' and c3N2.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3N5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3G1.cget("bg") =='green' and c3G2.cget("bg") =='green' and c3G3.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c3O1.cget("bg") =='green' and c3O2.cget("bg") =='green' and c3O3.cget("bg") =='green' and c3O4.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4B2.cget("bg") =='green' and c4B3.cget("bg") =='green' and c4B4.cget("bg") =='green' and c4B5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4I1.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4I5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4N1.cget("bg") =='green' and c4N2.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4N5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4G1.cget("bg") =='green' and c4G2.cget("bg") =='green' and c4G3.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)
        if c4O1.cget("bg") =='green' and c4O2.cget("bg") =='green' and c4O3.cget("bg") =='green' and c4O4.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won vertically on "+ cardwon)

    '''Check for win with Diagonal'''
    if chkdiagonal.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)
        if c1B5.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1G2.cget("bg") =='green' and c1O1.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)
        if c2B5.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2G2.cget("bg") =='green' and c2O1.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        #Card 3
        if c3B1.cget("bg") == 'green' and c3I2.cget("bg") == 'green' and c3N3.cget("bg") == 'green' and c3G4.cget("bg") == 'green' and c3O5.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Diagonally on " + cardwon)
        if c3B5.cget("bg") == 'green' and c3I4.cget("bg") == 'green' and c3N3.cget("bg") == 'green' and c3G2.cget("bg") == 'green' and c3O1.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)

        # Card 4
        if c4B1.cget("bg") == 'green' and c4I2.cget("bg") == 'green' and c4N3.cget("bg") == 'green' and c4G4.cget("bg") == 'green' and c4O5.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Diagonally on " + cardwon)
        if c4B5.cget("bg") == 'green' and c4I4.cget("bg") == 'green' and c4N3.cget("bg") == 'green' and c4G2.cget("bg") == 'green' and c4O1.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text = str(num_listo2["text"]) + "\n" + "You won Diagonally on "+ cardwon)


    '''Check for win with 4 Corners'''
    if chkcorners.get() ==1:
        #Card 1
        if c1B1.cget("bg") == 'green' and c1B5.cget("bg") == 'green' and c1O1.cget("bg") == 'green' and c1O5.cget("bg") == 'green':
            cardwon = 'Card 1!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 2
        if c2B1.cget("bg") == 'green' and c2B5.cget("bg") == 'green' and c2O1.cget("bg") == 'green' and c2O5.cget("bg") == 'green':
            cardwon = 'Card 2!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 3
        if c3B1.cget("bg") == 'green' and c3B5.cget("bg") == 'green' and c3O1.cget("bg") == 'green' and c3O5.cget("bg") == 'green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

        #Card 4
        if c4B1.cget("bg") == 'green' and c4B5.cget("bg") == 'green' and c4O1.cget("bg") == 'green' and c4O5.cget("bg") == 'green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won 4 corners on " + cardwon)

    '''Check for Cover all'''
    if chkcoverall.get() ==1:
        #Card 1
        if c1B1.cget("bg") =='green' and c1B2.cget("bg") =='green' and c1B3.cget("bg") =='green' and c1B4.cget("bg") =='green' and c1B5.cget("bg") =='green' \
            and c1I2.cget("bg") =='green' and c1I2.cget("bg") =='green' and c1I3.cget("bg") =='green' and c1I4.cget("bg") =='green' and c1I5.cget("bg") =='green' \
            and c1N3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N3.cget("bg") =='green' and c1N4.cget("bg") =='green' and c1N5.cget("bg") =='green' \
            and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G4.cget("bg") =='green' and c1G5.cget("bg") =='green' \
            and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green' and c1O5.cget("bg") =='green':
            cardwon = 'Card 1!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 2
        if c2B1.cget("bg") =='green' and c2B2.cget("bg") =='green' and c2B3.cget("bg") =='green' and c2B4.cget("bg") =='green' and c2B5.cget("bg") =='green' \
            and c2I2.cget("bg") =='green' and c2I2.cget("bg") =='green' and c2I3.cget("bg") =='green' and c2I4.cget("bg") =='green' and c2I5.cget("bg") =='green' \
            and c2N3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N3.cget("bg") =='green' and c2N4.cget("bg") =='green' and c2N5.cget("bg") =='green' \
            and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G4.cget("bg") =='green' and c2G5.cget("bg") =='green' \
            and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green' and c2O5.cget("bg") =='green':
            cardwon = 'Card 2!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 3
        if c3B1.cget("bg") =='green' and c3B2.cget("bg") =='green' and c3B3.cget("bg") =='green' and c3B4.cget("bg") =='green' and c3B5.cget("bg") =='green' \
            and c3I2.cget("bg") =='green' and c3I2.cget("bg") =='green' and c3I3.cget("bg") =='green' and c3I4.cget("bg") =='green' and c3I5.cget("bg") =='green' \
            and c3N3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N3.cget("bg") =='green' and c3N4.cget("bg") =='green' and c3N5.cget("bg") =='green' \
            and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G4.cget("bg") =='green' and c3G5.cget("bg") =='green' \
            and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green' and c3O5.cget("bg") =='green':
            cardwon = 'Card 3!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)

        #Card 4
        if c4B1.cget("bg") =='green' and c4B2.cget("bg") =='green' and c4B3.cget("bg") =='green' and c4B4.cget("bg") =='green' and c4B5.cget("bg") =='green' \
            and c4I2.cget("bg") =='green' and c4I2.cget("bg") =='green' and c4I3.cget("bg") =='green' and c4I4.cget("bg") =='green' and c4I5.cget("bg") =='green' \
            and c4N3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N3.cget("bg") =='green' and c4N4.cget("bg") =='green' and c4N5.cget("bg") =='green' \
            and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G4.cget("bg") =='green' and c4G5.cget("bg") =='green' \
            and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green' and c4O5.cget("bg") =='green':
            cardwon = 'Card 4!'
            num_listo2.config(text=str(num_listo2["text"]) + "\n" + "You won Cover-All on " + cardwon)


if __name__ == '__main__':
    listC1B=generate_c1B()
    listC1I=generate_c1I()
    listC1N=generate_c1N()
    listC1G=generate_c1G()
    listC1O=generate_c1O()

    listC2B=generate_c2B()
    listC2I=generate_c2I()
    listC2N=generate_c2N()
    listC2G=generate_c2G()
    listC2O=generate_c2O()

    listC3B=generate_c3B()
    listC3I=generate_c3I()
    listC3N=generate_c3N()
    listC3G=generate_c3G()
    listC3O=generate_c3O()

    listC4B=generate_c4B()
    listC4I=generate_c4I()
    listC4N=generate_c4N()
    listC4G=generate_c4G()
    listC4O=generate_c4O()

    main_win = Tk()
    main_win['bg']='gray'
    main_win.title('Your Bingo Bord')

    num_list = Tk()
    num_list.title('Number List')

    num_lista= Canvas(num_list, width = 200, height=100)
    num_listo1=Label(num_list,text="These numbers have been entered:")
    num_listo1.grid(row=0,column=0)
    num_listo2=Label(num_list,text="")
    num_listo2.grid(row=1,column=0)

    # Card 1 Column B
    c1 = Canvas(main_win, width=200, height=100, bg='white')
    c1B0 = Label(text="B", width=4, borderwidth=1, relief="groove").grid(row=0, column=0)
    c1B1 = Label(text=listC1B[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1B1.grid(row=1, column=0)
    c1B2 = Label(text=listC1B[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1B2.grid(row=2, column=0)
    c1B3 = Label(text=listC1B[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1B3.grid(row=3, column=0)
    c1B4 = Label(text=listC1B[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1B4.grid(row=4, column=0)
    c1B5 = Label(text=listC1B[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1B5.grid(row=5, column=0)

    # Card 1 Column I
    c1 = Canvas(main_win, width=200, height=100, bg='white')
    c1I0 = Label(text="I", width=4, borderwidth=1, relief="groove").grid(row=0, column=1)
    c1I1 = Label(text=listC1I[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1I1.grid(row=1, column=1)
    c1I2 = Label(text=listC1I[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1I2.grid(row=2, column=1)
    c1I3 = Label(text=listC1I[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1I3.grid(row=3, column=1)
    c1I4 = Label(text=listC1I[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1I4.grid(row=4, column=1)
    c1I5 = Label(text=listC1I[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1I5.grid(row=5, column=1)

    # Card 1 Column N
    c1 = Canvas(main_win, width=200, height=100, bg='white')
    c1N0 = Label(text="N", width=4, borderwidth=1, relief="groove").grid(row=0, column=2)
    c1N1 = Label(text=listC1N[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1N1.grid(row=1, column=2)
    c1N2 = Label(text=listC1N[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1N2.grid(row=2, column=2)
    c1N3 = Label(text="Free", width=4, borderwidth=1, relief="groove", bg="green", fg="white")
    c1N3.grid(row=3, column=2)
    c1N4 = Label(text=listC1N[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1N4.grid(row=4, column=2)
    c1N5 = Label(text=listC1N[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1N5.grid(row=5, column=2)

    # Card 1 Column G
    c1 = Canvas(main_win, width=200, height=100, bg='white')
    c1G0 = Label(text="G", width=4, borderwidth=1, relief="groove").grid(row=0, column=3)
    c1G1 = Label(text=listC1G[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1G1.grid(row=1, column=3)
    c1G2 = Label(text=listC1G[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1G2.grid(row=2, column=3)
    c1G3 = Label(text=listC1G[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1G3.grid(row=3, column=3)
    c1G4 = Label(text=listC1G[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1G4.grid(row=4, column=3)
    c1G5 = Label(text=listC1G[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1G5.grid(row=5, column=3)

    # Card 1 Column O
    c1 = Canvas(main_win, width=200, height=100, bg='white')
    c1O0 = Label(text="O", width=4, borderwidth=1, relief="groove").grid(row=0, column=4)
    c1O1 = Label(text=listC1O[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1O1.grid(row=1, column=4)
    c1O2 = Label(text=listC1O[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1O2.grid(row=2, column=4)
    c1O3 = Label(text=listC1O[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1O3.grid(row=3, column=4)
    c1O4 = Label(text=listC1O[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1O4.grid(row=4, column=4)
    c1O5 = Label(text=listC1O[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c1O5.grid(row=5, column=4)

    #Whitespace
    whitesp1 = Canvas(main_win, width=200, height=100, bg='gray')
    ws1 = Label(text="", width=4).grid(row=0, column=5)
    ws2 = Label(text="", width=4).grid(row=1, column=5)
    ws3 = Label(text="", width=4).grid(row=2, column=5)
    ws4 = Label(text="", width=4).grid(row=3, column=5)
    ws5 = Label(text="", width=4).grid(row=4, column=5)
    ws6 = Label(text="", width=4).grid(row=5, column=5)


    # Card 2 Column B
    c2 = Canvas(main_win, width=200, height=100, bg='gray')
    c2B0 = Label(text="B", width=4, borderwidth=1, relief="groove").grid(row=0, column=6)
    c2B1 = Label(text=listC2B[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2B1.grid(row=1, column=6)
    c2B2 = Label(text=listC2B[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2B2.grid(row=2, column=6)
    c2B3 = Label(text=listC2B[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2B3.grid(row=3, column=6)
    c2B4 = Label(text=listC2B[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2B4.grid(row=4, column=6)
    c2B5 = Label(text=listC2B[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2B5.grid(row=5, column=6)

    # Card 2 Column I
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c2I0 = Label(text="I", width=4, borderwidth=1, relief="groove").grid(row=0, column=7)
    c2I1 = Label(text=listC2I[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2I1.grid(row=1, column=7)
    c2I2 = Label(text=listC2I[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2I2.grid(row=2, column=7)
    c2I3 = Label(text=listC2I[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2I3.grid(row=3, column=7)
    c2I4 = Label(text=listC2I[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2I4.grid(row=4, column=7)
    c2I5 = Label(text=listC2I[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2I5.grid(row=5, column=7)

    # Card 2 Column N
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c2N0 = Label(text="N", width=4, borderwidth=1, relief="groove").grid(row=0, column=8)
    c2N1 = Label(text=listC2N[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2N1.grid(row=1, column=8)
    c2N2 = Label(text=listC2N[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2N2.grid(row=2, column=8)
    c2N3 = Label(text="Free", width=4, borderwidth=1, relief="groove", bg="green", fg="white")
    c2N3.grid(row=3, column=8)
    c2N4 = Label(text=listC2N[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2N4.grid(row=4, column=8)
    c2N5 = Label(text=listC2N[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2N5.grid(row=5, column=8)

    # Card 2 Column G
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c2G0 = Label(text="G", width=4, borderwidth=1, relief="groove").grid(row=0, column=9)
    c2G1 = Label(text=listC2G[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2G1.grid(row=1, column=9)
    c2G2 = Label(text=listC2G[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2G2.grid(row=2, column=9)
    c2G3 = Label(text=listC2G[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2G3.grid(row=3, column=9)
    c2G4 = Label(text=listC2G[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2G4.grid(row=4, column=9)
    c2G5 = Label(text=listC2G[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2G5.grid(row=5, column=9)

    # Card 2 Column O
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c2O0 = Label(text="O", width=4, borderwidth=1, relief="groove").grid(row=0, column=10)
    c2O1 = Label(text=listC2O[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2O1.grid(row=1, column=10)
    c2O2 = Label(text=listC2O[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2O2.grid(row=2, column=10)
    c2O3 = Label(text=listC2O[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2O3.grid(row=3, column=10)
    c2O4 = Label(text=listC2O[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2O4.grid(row=4, column=10)
    c2O5 = Label(text=listC2O[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c2O5.grid(row=5, column=10)

    # Whitespace
    whitesp2 = Canvas(main_win, width=200, height=100, bg='gray')
    ws = Label(text="", width=4,bg='gray').grid(row=6, column=1)
    ws7 = Label(text="", width=4,bg='gray').grid(row=6, column=2)
    ws8 = Label(text="", width=4,bg='gray').grid(row=6, column=3)
    ws9 = Label(text="", width=4,bg='gray').grid(row=6, column=4)
    ws10 = Label(text="", width=4,bg='gray').grid(row=6, column=5)
    ws11 = Label(text="", width=4,bg='gray').grid(row=6, column=6)
    ws12 = Label(text="", width=4,bg='gray').grid(row=6, column=7)
    ws13 = Label(text="", width=4,bg='gray').grid(row=6, column=8)
    ws14 = Label(text="", width=4,bg='gray').grid(row=6, column=9)
    ws15 = Label(text="", width=4,bg='gray').grid(row=6, column=10)
    ws16 = Label(text="", width=4,bg='gray').grid(row=6, column=11)

    # Card 3 Column B
    c3 = Canvas(main_win, width=200, height=100, bg='gray')
    c3B0 = Label(text="B", width=4, borderwidth=1, relief="groove").grid(row=7, column=0)
    c3B1 = Label(text=listC3B[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3B1.grid(row=8, column=0)
    c3B2 = Label(text=listC3B[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3B2.grid(row=9, column=0)
    c3B3 = Label(text=listC3B[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3B3.grid(row=10, column=0)
    c3B4 = Label(text=listC3B[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3B4.grid(row=11, column=0)
    c3B5 = Label(text=listC3B[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3B5.grid(row=12, column=0)

    # Card 3 Column I
    c3 = Canvas(main_win, width=200, height=100, bg='white')
    c3I0 = Label(text="I", width=4, borderwidth=1, relief="groove").grid(row=7, column=1)
    c3I1 = Label(text=listC3I[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3I1.grid(row=8, column=1)
    c3I2 = Label(text=listC3I[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3I2.grid(row=9, column=1)
    c3I3 = Label(text=listC3I[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3I3.grid(row=10, column=1)
    c3I4 = Label(text=listC3I[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3I4.grid(row=11, column=1)
    c3I5 = Label(text=listC3I[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3I5.grid(row=12, column=1)

    # Card 3 Column N
    c3 = Canvas(main_win, width=200, height=100, bg='white')
    c3N0 = Label(text="N", width=4, borderwidth=1, relief="groove").grid(row=7, column=2)
    c3N1 = Label(text=listC3N[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3N1.grid(row=8, column=2)
    c3N2 = Label(text=listC3N[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3N2.grid(row=9, column=2)
    c3N3 = Label(text="Free", width=4, borderwidth=1, relief="groove", bg="green", fg="white")
    c3N3.grid(row=10, column=2)
    c3N4 = Label(text=listC3N[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3N4.grid(row=11, column=2)
    c3N5 = Label(text=listC3N[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3N5.grid(row=12, column=2)

    # Card 3 Column G
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c3G0 = Label(text="G", width=4, borderwidth=1, relief="groove").grid(row=7, column=3)
    c3G1 = Label(text=listC3G[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3G1.grid(row=8, column=3)
    c3G2 = Label(text=listC3G[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3G2.grid(row=9, column=3)
    c3G3 = Label(text=listC3G[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3G3.grid(row=10, column=3)
    c3G4 = Label(text=listC3G[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3G4.grid(row=11, column=3)
    c3G5 = Label(text=listC3G[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3G5.grid(row=12, column=3)

    # Card 3 Column O
    c2 = Canvas(main_win, width=200, height=100, bg='white')
    c3O0 = Label(text="O", width=4, borderwidth=1, relief="groove").grid(row=7, column=4)
    c3O1 = Label(text=listC3O[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3O1.grid(row=8, column=4)
    c3O2 = Label(text=listC3O[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3O2.grid(row=9, column=4)
    c3O3 = Label(text=listC3O[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3O3.grid(row=10, column=4)
    c3O4 = Label(text=listC3O[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3O4.grid(row=11, column=4)
    c3O5 = Label(text=listC3O[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c3O5.grid(row=12, column=4)

    chkhorizontal = IntVar()
    chkvertical = IntVar()
    chkdiagonal = IntVar()
    chkcorners = IntVar()
    chkcoverall = IntVar()


    # Whitespace
    whitesp3 = Canvas(main_win, width=200, height=100, bg='white')
    ws17 = Label(text="Please select win conditions:", width=25,anchor='w',bg='azure2').grid(row=0, column=5)
    chkhor = Checkbutton(text="Horizontal",variable = chkhorizontal,onvalue = 1,width=22,anchor='w',bg='azure2',fg='blue')
    chkhor.grid(row=1, column=5)
    chkver = Checkbutton(text="Vertical",variable = chkvertical,onvalue = 1,width=22,anchor='w',bg='azure2',fg='blue')
    chkver.grid(row=2, column=5)
    chkdiag = Checkbutton(text="Diagonal",variable = chkdiagonal,onvalue = 1,width=22,anchor='w',bg='azure2',fg='blue')
    chkdiag.grid(row=3, column=5)
    chkcorn = Checkbutton(text="4 Corners",variable = chkcorners,onvalue = 1,width=22,anchor='w',bg='azure2',fg='blue')
    chkcorn.grid(row=4, column=5)
    chkcvr = Checkbutton(text="Cover all",variable = chkcoverall,onvalue = 1,width=22,anchor='w',bg='azure2',fg='blue')
    chkcvr.grid(row=5, column=5)



    # Card 4 Column B
    c4 = Canvas(main_win, width=200, height=100, bg='white')
    c4B0 = Label(text="B", width=4, borderwidth=1, relief="groove").grid(row=7, column=6)
    c4B1 = Label(text=listC4B[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4B1.grid(row=8, column=6)
    c4B2 = Label(text=listC4B[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4B2.grid(row=9, column=6)
    c4B3 = Label(text=listC4B[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4B3.grid(row=10, column=6)
    c4B4 = Label(text=listC4B[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4B4.grid(row=11, column=6)
    c4B5 = Label(text=listC4B[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4B5.grid(row=12, column=6)

    # Card 4 Column I
    c4 = Canvas(main_win, width=200, height=100, bg='white')
    c4I0 = Label(text="I", width=4, borderwidth=1, relief="groove").grid(row=7, column=7)
    c4I1 = Label(text=listC4I[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4I1.grid(row=8, column=7)
    c4I2 = Label(text=listC4I[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4I2.grid(row=9, column=7)
    c4I3 = Label(text=listC4I[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4I3.grid(row=10, column=7)
    c4I4 = Label(text=listC4I[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4I4.grid(row=11, column=7)
    c4I5 = Label(text=listC4I[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4I5.grid(row=12, column=7)

    # Card 4 Column N
    c4 = Canvas(main_win, width=200, height=100, bg='white')
    c4N0 = Label(text="N", width=4, borderwidth=1, relief="groove").grid(row=7, column=8)
    c4N1 = Label(text=listC4N[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4N1.grid(row=8, column=8)
    c4N2 = Label(text=listC4N[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4N2.grid(row=9, column=8)
    c4N3 = Label(text="Free", width=4, borderwidth=1, relief="groove", bg="green", fg="white")
    c4N3.grid(row=10, column=8)
    c4N4 = Label(text=listC4N[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4N4.grid(row=11, column=8)
    c4N5 = Label(text=listC4N[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4N5.grid(row=12, column=8)

    # Card 4 Column G
    c4 = Canvas(main_win, width=200, height=100, bg='white')
    c4G0 = Label(text="G", width=4, borderwidth=1, relief="groove").grid(row=7, column=9)
    c4G1 = Label(text=listC4G[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4G1.grid(row=8, column=9)
    c4G2 = Label(text=listC4G[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4G2.grid(row=9, column=9)
    c4G3 = Label(text=listC4G[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4G3.grid(row=10, column=9)
    c4G4 = Label(text=listC4G[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4G4.grid(row=11, column=9)
    c4G5 = Label(text=listC4G[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4G5.grid(row=12, column=9)

    # Card 4 Column O
    c4 = Canvas(main_win, width=200, height=100, bg='white')
    c4O0 = Label(text="O", width=4, borderwidth=1, relief="groove").grid(row=7, column=10)
    c4O1 = Label(text=listC4O[0], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4O1.grid(row=8, column=10)
    c4O2 = Label(text=listC4O[1], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4O2.grid(row=9, column=10)
    c4O3 = Label(text=listC4O[2], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4O3.grid(row=10, column=10)
    c4O4 = Label(text=listC4O[3], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4O4.grid(row=11, column=10)
    c4O5 = Label(text=listC4O[4], width=4, borderwidth=1, relief="groove", bg="red", fg="white")
    c4O5.grid(row=12, column=10)

    # Whitespace
    whitesp4 = Canvas(main_win, width=200, height=100, bg='white')
    ws23 = Label(text="", width=4,bg='gray').grid(row=13, column=1)
    ws24 = Label(text="", width=4,bg='gray').grid(row=13, column=2)
    ws25 = Label(text="", width=4,bg='gray').grid(row=13, column=3)
    ws26 = Label(text="", width=4,bg='gray').grid(row=13, column=4)
    ws27 = Label(text="", width=4,bg='gray').grid(row=13, column=5)
    ws28 = Label(text="", width=4,bg='gray').grid(row=13, column=6)
    ws29 = Label(text="", width=4,bg='gray').grid(row=13, column=7)
    ws30 = Label(text="", width=4,bg='gray').grid(row=13, column=8)
    ws31 = Label(text="", width=4,bg='gray').grid(row=13, column=9)
    ws32 = Label(text="", width=4,bg='gray').grid(row=13, column=10)

    EnterNumber = Label(text="Enter a number",fg='white',bg='blue').grid(row=14, column=5)
    NumberEntry = Entry(text="")
    NumberEntry.grid(row=15, column=5)
    Submit = Button(text="Submit",bg='green',fg='white',command=button_is_match).grid(row=16, column=5)
    main_win.bind('<Return>', enter_is_match)

    main_win.mainloop()