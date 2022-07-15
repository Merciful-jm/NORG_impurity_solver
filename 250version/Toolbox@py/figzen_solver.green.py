import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(fname = './data/solver.green.dat')
x    = []
real = []
imag = []
for i in range(1024):
    for j in range(5):
        if j == 2:
            x.append(data[i][j])
        if j == 3:
            real.append(data[i][j])
        if j == 4:
            imag.append(data[i][j])

fig, ax = plt.subplots()
ax.plot(x, real)
plt.xlabel("omega")
plt.ylabel("real")
plt.title("iQst solver data")
fig, ay = plt.subplots()
ay.plot(x, imag)
plt.xlabel("omega")
plt.ylabel("image")
plt.title("iQst solver data")
plt.show()
