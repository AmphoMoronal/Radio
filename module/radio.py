import multiprocessing
from playsound import playsound
import os

hr1 = 'https://dispatcher.rndfnk.com/hr/hr1/live/mp3/high'
hr3 = 'https://dispatcher.rndfnk.com/hr/hr3/live/mp3/high'
hr4 = 'https://dispatcher.rndfnk.com/hr/hr4/mitte/mp3/high'
absolut_relax = 'https://absolut-relax.live-sm.absolutradio.de/absolut-relax/stream/mp3'

channels = [hr3, absolut_relax, hr1, hr4]
streams = []


def play(i=1):
    p = multiprocessing.Process(target=playsound, args=(channels[i],))
    streams.append(p)
    print(streams)
    p.start()


def kill():
    for stream in streams:
        streams.remove(stream)
        stream.terminate()


def restart():
    os.system("killall python3.10 && python3.10 main.py")
