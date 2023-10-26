import threading


def setTimeout(callback, delay):
    timer = threading.Timer(delay / 1000, callback)
    timer.start()


def myCallback():
    print("setTimeout callback executed")


setTimeout(myCallback, 1000)
setTimeout(myCallback, 2000)
