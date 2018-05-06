import numpy as np
import matplotlib.pyplot as plt

print('test project line 1')
print('test project line 2')
print('test project - end')

print('this is the new line added to the branch')
print('adding a second line')

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()

ax.fill(x, y, zorder=10)
ax.grid(True, zorder=5)
plt.show()
