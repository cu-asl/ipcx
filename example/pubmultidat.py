import ipcx
import time
ipc = ipcx.IPC("example2")

ipc.server("test")

tempDict = {"num" : 2,"point" :2.5, "str": "Hello World!"}


while ipc.isRun():
    msg = ipcx.toJson(tempDict)

    ipc.publish(msg,show = "on")

    #sleep 1 sec
    time.sleep(1)