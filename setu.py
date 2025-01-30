import numpy as np
import matplotlib.pyplot as plt

# 创建圆面
theta = np.linspace(0, 2*np.pi, 100)
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)

# 颜色渐变
colors = plt.cm.jet(np.linspace(0, 1, len(x)))

# 绘制圆面
fig, ax = plt.subplots()
for i in range(len(x) - 1):
    ax.fill([0, x[i], x[i+1]], [0, y[i], y[i+1]], color=colors[i], edgecolor='white')
ax.fill([0, x[-1], x[0]], [0, y[-1], y[0]], color=colors[-1], edgecolor='white')

# 添加颜色说明文字
m=60
n=60
line_spacing=0.1
row = i // n
col = i % n
for i in range(len(colors)):
    ax.text(1.1, 1-i*(3/len(colors)), f'Color {i}', color=colors[i],fontsize=4)
#    ax.text(1.1, 1-i*(line_spacing + 0.1), f'Color {i}', color=colors[i])
#    ax.text(1.1 + col * 0.5, 1 - row * (line_spacing + 0.1), f'Color {i}', color=colors[i], fontsize=10)

plt.axis('equal')
plt.axis('off')
plt.show()