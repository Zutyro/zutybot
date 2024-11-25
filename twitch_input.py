import socket
from time import time
from datetime import datetime


def twitch_connect(login, oauth, channel):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('irc.chat.twitch.tv', 6667))
    print('Connected')
    s.send(str.encode(f'PASS {oauth}\r\n'))
    s.send(str.encode(f'NICK {login}\r\n'))
    s.send(str.encode(f'JOIN #{channel}\r\n'))
    s.send(str.encode('CAP REQ twitch.tv/membership\r\n'))
    return s


def twitch_input(channel, s):
    message = s.recv(4096).decode("UTF-8")
    print(message)
    s.send(str.encode(f'PRIVMSG #{channel} :ZutyBot Online MrDestructoid\r\n'))
    cluelesscount = 0
    lastclueless = 0
    while True:
        message = ""
        privmsg = ""
        texts = ""
        message = s.recv(4096).decode("UTF-8")
        print(message)
        if message == "PING :tmi.twitch.tv\r\n":
            print("PINGING IRC")
            s.send(str.encode('PONG :tmi.twitch.tv\r\n'))
            continue
        texts = message.split(":")

        if ("JOIN" in texts[1] or "PART" in texts[1]) and "zutybot" not in texts[1]:
            print("Userlist has changed")
            for text in texts[1:]:
                join = text.split("!")
                username = join[0]
                if "JOIN" in join[1]:
                    print(f"{username} has connected")
                if "PART" in join[1]:
                    print(f"{username} has disconnected")

        if len(texts) > 2 and texts[2] == "!test\r\n":
            print("Responding to test")
            s.send(str.encode(f'PRIVMSG #{channel} :Test akceptován MrDestructoid\r\n'))

        if len(texts) > 2 and "Clueless" in texts[2] and (time() - lastclueless) > 300:
            print("Clueless moment")
            lastclueless = time()
            s.send(str.encode(f'PRIVMSG #{channel} :Clueless okamžik\r\n'))


def twitch_bedge(channel, s):
    lastmin = 0
    while True:
        dt = datetime.now()
        if lastmin != dt.minute:
            lastmin = dt.minute
            print(f"Current time: {dt.hour}:{dt.minute}")
            if dt.hour == 0 and dt.minute == 0:
                print("Bedge time")
                s.send(str.encode(f'PRIVMSG #{channel} :00:00 Bedge\r\n'))
            if dt.hour == 0 and dt.minute == 1:
                print("Wokege time")
                s.send(str.encode(f'PRIVMSG #{channel} :00:01 Wokege\r\n'))



