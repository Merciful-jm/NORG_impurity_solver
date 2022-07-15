import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(fname = './data/zic001.mb.hb_final.txt', skiprows=1)
x    = []
real = []
imag = []
for i in range(len(data)):
    for j in range(4):
        if j == 0:
            x.append(data[i][j])
        if j == 1:
            real.append(data[i][j])
        if j == 3:
            imag.append(data[i][j])
# real = -1*real
# imag = -1*imag
fig, ax = plt.subplots()
ax.plot(x, real)
plt.xlabel("omega")
plt.ylabel("real")
plt.title("NORG solver data")
fig, ay = plt.subplots()
ay.plot(x, imag)
plt.xlabel("omega")
plt.ylabel("image")
plt.title("NORG solver data")
plt.show()
