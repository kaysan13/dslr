#!/usr/bin/env python

from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess


# Kill the gphoto process that starts
# whenever we turn on the camera or
# reboot the raspberry pi

def killGphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Search for the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill that process!
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


shot_date = datetime.now().strftime("%Y-%m-%d")  # This has been written to the while True loop.
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # This has been written to the while True loop.

triggerCommand = ["--trigger-capture"]
downloadFileCommand = ["--capture-image-and-download"]

save_location = "/home/pi/images/" + shot_date


def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to create new directory.")


def getCameraInfo():
    camera = gp('-a')
    print(camera)


def captureImages():
    gp(downloadFileCommand)
    sleep(3)


def renameFiles(ID):
    for filename in os.listdir("."):
        if filename.endswith(".jpg"):
            os.rename(filename, (save_location + "/" + shot_time + ".jpg"))
            print("Moved the JPG")
        elif filename.endswith(".cr2"):
            os.rename(filename, (save_location + "/" + shot_time + ".cr2"))
            print("Moved the CR2")


getCameraInfo()
captureImages()
createSaveFolder()
renameFiles(save_location)
killGphoto2Process()
