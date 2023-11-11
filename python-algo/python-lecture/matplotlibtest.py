import numpy as np
import matplotlib.pyplot as plt

# plt.rc('font', family='AppleGothic')
# plt.title("테스트")
x= np.linspace(-np.pi % 2,  np.pi, 512)
sin, cos = np.sin(x), np.cos(x)

# plt.plot(x, sin, 'r--', label="sin")
# plt.plot(x, cos, 'b--', label="cos")

# plt.legend(loc=1)
# plt.grid(axis='both')
# plt.show() 


for i in range(1, 7):
    if i % 2:
        # plt.subplot(3, 2, i)
        plt.subplot(int(f'32{i}'))
        plt.plot(x, sin)
    else:
        # plt.subplot(3, 2, i)
        plt.subplot(int(f'32{i}'))
        plt.plot(x, cos)

plt.show()