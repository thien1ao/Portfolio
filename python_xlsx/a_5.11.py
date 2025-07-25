import matplotlib.pyplot as plt
import numpy as np

mod = 10 ** -6


def integrand(t):
    return np.exp(-t**2/2)


def trapez(phi, a=0, b=1, n=100):
    x_vals = np.linspace(a, b, n+1)
    y = phi(x_vals)
    mid = (b-a)/n

    y_l = y[1:]
    y_r = y[:-1]

    return (mid/2) * np.sum(y_l + y_r)


def trapez_error(phi, a=0, b=1, n=100):
    prev = trapez(phi, a, b, n)
    while True:
        n *= 2
        current = trapez(phi, a, b, n)
        if (current - prev) < mod:
            break
        prev = current

    return current


x = np.linspace(0, 1, 10000)
y = 1/2 + 1/np.sqrt(2 * np.pi) * integrand(x)
plt.plot(x, y, color="cornflowerblue")
plt.grid(True)
plt.show()


print(1/2 + 1/np.sqrt((2 * np.pi)) * trapez_error(lambda t: np.exp(-t**2/2), 0, 1, 10000))
