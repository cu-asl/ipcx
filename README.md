# IPCx

IPCx stands for Inter-process communication x.

The IPCx is a set of libraries and tools for Inter-process communication.
Our IPC type is publish–subscribe pattern. Now we are developing it with **matlab** and **python3** which are based on **ROS** .
The IPCx runs python3 on WSL but runs matlab on Windows 10. 

## Version of Software
We developed on
software|version
----------- | -------------
WSL |Ubuntu 20.04 LTS
Python | Python 3.8.2 64 bit
Matlab| 2020a
ROS | ROS Noetic Ninjemys (ROS 1)

Moreover, IPCx require **ROS Toolbox** on Matlab.
* For more information about ROS Toolbox: [https://www.mathworks.com/products/ros.html](https://www.mathworks.com/products/ros.html)

* For installation of ROS Toolbox: [https://www.mathworks.com/help/ros/ug/install-robotics-system-toolbox-support-packages.html](https://www.mathworks.com/help/ros/ug/install-robotics-system-toolbox-support-packages.html)

## Installation
1.Install WSL, Python3, Matlab 

2.Install [ROS](http://wiki.ros.org/noetic/Installation/Ubuntu)

> you can see our ROS installation tutorial at [https://github.com/CUASL/ipcx/wiki/Installation](https://github.com/CUASL/ipcx/wiki/Installation)

3.Copy our library folder [ipcx](https://github.com/CUASL/ipcx/tree/master/ipcx) on our github
to your project directory so that you can use our library.

4.import our library in your code
    
python
```python
import ipcx
```
matlab
```matlab
addpath('ipcx')
```

## Usage
You can get start and see more tutorial [wiki](https://github.com/CUASL/ipcx/wiki)

### How to run
This example will show case server: python and client: matlab

*    **step** 1 open WSL
```bash
roscore
```

*   **step 2** open another WSL and run your serverfile 
```bash
python3 yourServerFileName.py
```

*For Example in example directory*
```bash
python3 ex_publisher.py
```

*   **step 3** open matlab and run your client file

*for example(run in matlab bash or you can click run at matlab UI)*
```matlab
ex_subscriber
```

## Supported platforms and languages
- platforms
  - Windows 10 with WSL
  - Linux/Ubuntu
- Languages
  - Python3
  - Matlab
