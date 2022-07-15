import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(fname = './data/zic001.mb.hby_i.txt', skiprows=1)

x    = []
real = []
imag = []
for i in range(len(data)):
    for j in range(4):
        if j == 0:
            x.append(data[i][j])
        if j == 1:
            real.append(-data[i][j])
        if j == 3:
            imag.append(-data[i][j])

datafit = np.loadtxt(fname = './data/zic001.mb.hb_fitting.txt', skiprows=1)
x_fit    = []
real_fit = []
imag_fit = []
for i in range(len(data)):
    for j in range(4):
        if j == 0:
            x_fit.append(data[i][j])
        if j == 1:
            real_fit.append(-data[i][j])
        if j == 3:
            imag_fit.append(-data[i][j])

fig, ax = plt.subplots()
ax.plot(x, real, linewidth=3.5, label='input')
ax.plot(x_fit, real_fit,  label='fitting')
plt.xlabel("omega")
plt.ylabel("real")
plt.title("NORG solver data")
plt.legend()
fig, ay = plt.subplots()
ay.plot(x, imag, linewidth=3.5, label='input')
ay.plot(x_fit, imag_fit,  label='fitting')
plt.xlabel("omega")
plt.ylabel("image")
plt.title("NORG solver data")
plt.legend()
plt.show()
