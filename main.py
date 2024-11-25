import threading
import asyncio
from twitch_input import twitch_connect, twitch_input, twitch_bedge

login = "zutybot"
oauth = "oauth:9p77nvdoin37i158kx43pr23hibw2h"
channel = "forevermelounkdr"


def main():
    s = twitch_connect(login, oauth, channel)
    bedge = threading.Thread(target=twitch_bedge, args=[channel, s])
    bedge.start()
    input = threading.Thread(target=twitch_input, args=[channel, s])
    input.start()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

