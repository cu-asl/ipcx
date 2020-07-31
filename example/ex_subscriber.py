import ipcx


def callbackfx(msg):

    print(msg.data)

ipc = ipcx.IPC("example_sub")

#-------- start client : subscribe topic : "test"  --------#
#cli = ipc.client("test",callbackfx)
cli = ipcx.client("test")
ipc.spin()
