import numpy as np
import matplotlib.pyplot as plt

simulation_number = 10000


def gen_array(ch: str) -> np.ndarray:
    return np.full(8, ch)


cards = np.concatenate((gen_array('b'), gen_array('p'), gen_array('t'), gen_array('h')))

counter = 0
res = []

for i in range(simulation_number):
    np.random.shuffle(cards)
    sp1 = cards[:10]
    sp2 = cards[10:20]

    b1 = np.count_nonzero(sp1 == 'b')
    b2 = np.count_nonzero(sp2 == 'b')

    if b1 == 2 and b2 == 2:
        counter += 1

    res.append(counter / (i + 1))

w = counter / simulation_number

# Plotten
plt.plot(res, color="cornflowerblue")
plt.axhline(y=w, color="orange", label=f"P: {w:.4f}")
plt.legend()
plt.grid(True)
plt.show()
