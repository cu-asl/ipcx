import ipcx
import time
ipc = ipcx.IPC("example2")

serv = ipcx.server("test")

tempDict = {"num" : 2,"point" :2.5, "str": "Hello World!"}


while ipc.isRun():
    msg = ipcx.toJson(tempDict)

    serv.publish(msg,show = "on")

    #sleep 1 sec
    time.sleep(1)