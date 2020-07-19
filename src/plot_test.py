## plot pkg
import numpy as np
import matplotlib.pyplot as plt

# _*_ coding: utf-8 _*_

"""
python_visual_animation.py by xianhu
"""

#import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt



def simple_plot():
    """
    simple plot
    """
    # 生成画布
    plt.figure(figsize=(8, 6), dpi=80)

    # 打开交互模式
    plt.ion()

    # 循环
    for index in range(100):
        # 清除原有图像
        plt.cla()

        # 设定标题等
        plt.title("aaa")
        plt.grid(True)

        # 生成测试数据
        x = np.linspace(-np.pi + 0.1*index, np.pi+0.1*index, 256, endpoint=True)
        y_cos, y_sin = np.cos(x), np.sin(x)

        # 设置X轴
        plt.xlabel("X")
        plt.xlim(-4 + 0.1*index, 4 + 0.1*index)
        plt.xticks(np.linspace(-4 + 0.1*index, 4+0.1*index, 9, endpoint=True))

        # 设置Y轴
        plt.ylabel("Y")
        plt.ylim(-1.0, 1.0)
        plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

        # 画两条曲线
        plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos")
        plt.plot(x, y_sin, "g-", linewidth=2.0, label="sin")

        # 设置图例位置,loc可以为[upper, lower, left, right, center]
        plt.legend(loc="upper left", shadow=True)

        # 暂停
        plt.pause(0.1)

    # 关闭交互模式
    plt.ioff()

    # 图形显示
    #plt.show()
    return


# simple_plot()

current_frame = [1,2,3]
current_frame2 = [1,2,3,4]
current_frame3 = [1,2,3,4,5]
test = [0 for i in range(40)]
print(f'{test}')
print(f'{type(test)}')
## plot params
plt.figure()
plt.ion()
plt.title("aaa")
plt.grid(True)

plt.ylabel("Y")
plt.ylim(0.0, 50.0)
#plt.yticks(np.linspace(0, 5, 9, endpoint=True))

# 画两条曲线
plt.ylabel("Y")
plt.ylim(0.0, 50.0)
plt.plot(current_frame, "b--", linewidth=2.0, label="cos")
plt.pause(1)
plt.cla()
plt.ylabel("Y")
plt.ylim(0.0, 50.0)
plt.plot(current_frame2, "b--", linewidth=2.0, label="cos")
plt.pause(1)
plt.cla()
plt.ylabel("Y")
plt.ylim(0.0, 50.0)
plt.plot(current_frame3, "b--", linewidth=2.0, label="cos")
plt.ioff()
plt.show()
#current_frame = np.zeros(40)
#previous_frame = np.zeros(40)
#print(f'current_frame: {current_frame}')
#plt.plot(current_frame)
#fig, ax = plt.subplots()
#line, = ax.plot(current_frame)
#ax.set_ylim(-3, 3)

#ax.set_ylabel("Voltage")
#ax.set_xlabel("time")
#plt.plot()
