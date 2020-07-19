import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def update(frame):
    global current_frame
    global previous_frame
    global line    
    #读入模拟
    a = np.random.rand()#*2-1
    #time.sleep(1/10)
    #绘图数据生成  
    alonzo=5
    current_frame[0:(-alonzo)] = previous_frame[alonzo:] # index 0 to index -1 = index 1 to last element
    current_frame[-1] = a
    previous_frame = current_frame
    #绘图 
    line.set_ydata(current_frame)    
    #颜色设置
    return line


# Fixing random state for reproducibility
np.random.seed()
#初始数据绘图
current_frame = np.zeros(40)
previous_frame = np.zeros(40)
fig, ax = plt.subplots()
line, = ax.plot(current_frame)
ax.set_ylim(-3, 3)
plt.grid(True)
ax.set_ylabel("Voltage")
ax.set_xlabel("time")

ani = animation.FuncAnimation(fig, update,frames=None, interval=1000)
plt.show()



