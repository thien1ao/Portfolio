import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

w_list: list[int] = []


def roll():
    return np.random.randint(1, 7)


def main(n):
    for _ in range(n):
        roll_10_list = [roll() for _ in range(10)]
        sum_ = sum(roll_10_list)
        w_list.append(sum_)


main(1000)

plt.hist(w_list, bins=range(10, 50), density=True, color="cornflowerblue", edgecolor="black", alpha=0.6)

kde = gaussian_kde(w_list)
x_vals = np.linspace(20, 60, 500)
kde_vals = kde(x_vals)
plt.plot(x_vals, kde_vals, color="orange", linewidth=2)

plt.grid(True)
plt.xlabel("Summe")
plt.ylabel("Wahrscheinlichkeit")
plt.show()
