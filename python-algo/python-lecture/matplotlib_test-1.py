import numpy as np
import matplotlib.pyplot as plt

grid = plt.GridSpec(2, 3, wspace = 0.5, hspace=0.3)
ax1 = plt.subplot(grid[0, 0])
ax2 = plt.subplot(grid[0, 1:])
ax3 = plt.subplot(grid[1, :2])
ax4 = plt.subplot(grid[1, 2])


# 객체를 얻어내서
# 객체를 통해 Plot을 그려주고
# 해당 ax1은 0행 0열을 그려주고 있기 떄문에
# ax1의 그림이 Plot으로 그려진다.
ax1.plot(np.arange(10))
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
ax2.plot(np.sin(x))
ax3.plot(np.cos(x))
ax4.bar(np.arange(10), np.random.randint(0, 100, 10))

plt.show()
