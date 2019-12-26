import os
import time


def creating(args1, args2):
    time_web = time.strftime('%Y-%m-%d')
    time_os = os.path.dirname(os.path.abspath(__file__))
    this_path = os.path.join(time_os, args1, args2)
    if not os.path.isdir(this_path):
        os.mkdir(this_path)
    time_path = os.path.join(this_path, time_web)
    return time_path

