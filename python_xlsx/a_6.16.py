import matplotlib.pyplot as plt
import numpy as np

res = []
counter = 0
simulation = 10000


def wurf():
    return np.random.randint(1, 7)


for i in range(simulation):
    list_ = [wurf() for _ in range(6)]
    sorted_list_ = np.sort(list_)
    l, r = 0, 1
    dupl = False

    while r < len(sorted_list_):
        if sorted_list_[r] == sorted_list_[l]:
            dupl = True
            break
        l += 1
        r += 1

    if dupl:
        counter += 1

    res.append(counter / (i + 1))


array = wurf()

w = counter/simulation

plt.plot(res, color="cornflowerblue")
plt.axhline(y=w, color="orange", label=f"P: {w:.2f}")
plt.legend()
plt.grid(True)
plt.show()
