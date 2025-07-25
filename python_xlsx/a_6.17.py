import matplotlib.pyplot as plt
import numpy as np
import itertools

simulation = 10000
res = []
counter = 0


def wurf():
    return np.random.randint(1, 7)


for i in range(simulation):
    wurfe = [wurf() for _ in range(6)]
    sorted(wurfe)

    if (len(wurfe) - len(set(wurfe)) == 3):
        counter += 1

    res.append(counter/(i + 1))

w = counter / simulation

plt.plot(res, color="cornflowerblue")
plt.axhline(y=w, color="orange", label=f"P: {w:.2f}")
plt.legend()
plt.grid(True)
plt.show()
