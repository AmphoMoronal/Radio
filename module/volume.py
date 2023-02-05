from subprocess import call, run
import os

output_device = "Master"


def get_volume():
    volume = os.popen("amixer get Master | grep -o [0-9]*%|sed 's/%//'").readline()
    return int(volume)


def set_volume(volume):
    call(["amixer", "-D", "pulse", "sset", "Master", f"{volume}%"])


def mute():
    call(["amixer", "-D", "pulse", "sset", "Master", "0%"])


def increase():
    call(["amixer", "-D", "pulse", "sset", "Master", "5%+"])


def decrease():
    call(["amixer", "-D", "pulse", "sset", "Master", "5%-"])

