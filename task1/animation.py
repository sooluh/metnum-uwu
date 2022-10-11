import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

sns.set()


def f(x):
    return 2.99*x**5-1.12*x**3-1.26


# global variabel untuk animasi grafik
root = 0


def bisection(a, b, e=10**-4, n=100):
    step = 1
    condition = True

    while condition:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        step = step + 1
        condition = abs(f(c)) > e and step <= n

    # tetapkan nilai dari variabel c ke variabel root (global variabel)
    root = c


a = float(1)
b = float(2)

if f(a) * f(b) > 0.0:
    print('Nilai yang diberikan harus diantara akar.')
else:
    bisection(a, b)


top = -1.125
bottom = 1.25

x = np.arange(top, bottom, 0.1)
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(xlim=(top, bottom), ylim=(min(f(x)), max(f(x))))

plt.yticks([], [])
ax.spines["bottom"].set_position(("data", 0))
ax.spines["bottom"].set_color('black')

sns.lineplot(x=x, y=f(x))

nodea, = ax.plot([a], [f(a)], 'yo', markersize=15)
nodeb, = ax.plot([b], [f(b)], 'go', markersize=15)
nodec, = ax.plot([root], [f(root)], 'ro', markersize=15)

ax.legend(['function', 'a', 'b', 'c'])


def draw(f, a, b, e=10**-4, n=100):
    if f(a) * f(b) >= 0:
        return None

    xa = np.array([])
    xb = np.array([])
    xc = np.array([])

    step = 1
    condition = True

    while condition:
        c = (a + b) / 2

        xa = np.append(xa, a)
        xb = np.append(xb, b)
        xc = np.append(xc, c)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        step = step + 1
        condition = abs(f(c)) > e and step <= n

    return xa, xb, xc


xa, xb, xc = draw(f, a, b)


def animate(i):
    nodea.set_data(xa[i], f(xa[i]))
    nodeb.set_data(xb[i], f(xb[i]))
    nodec.set_data(xc[i], f(xc[i]))

    return nodea, nodeb, nodec


plt.rcParams['animation.html'] = 'html5'
anim = animation.FuncAnimation(fig, animate, frames=len(xa), blit=False, repeat=True, interval=100)
plt.close()
anim.save('bisection.gif', writer='imagemagick', fps=18)
