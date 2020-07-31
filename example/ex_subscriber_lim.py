import ipcx
import rospy

count = 0
ipc = ipcx.IPC("example_sub")

def callbackfx(msg):
    global count
    count+=1 
    if count == 10:
        ipc.off()
    print(msg.data,count)



#-------- start client : subscribe topic : "test"  --------#
cli = ipcx.client("test",callbackfx)

ipc.spin()
