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
    found = False
    for j in range(len(cards) - 3):
        window = cards[j:j+4]
        if all(item == 'b' for item in window):
            found = True
            break
    if found:
        counter += 1
    res.append(counter / (i + 1))

w = counter / simulation_number

plt.plot(res, color="cornflowerblue")
plt.axhline(y=w, color="orange", label=f"P: {w:.2f}")
plt.legend()
plt.grid(True)
plt.show()
