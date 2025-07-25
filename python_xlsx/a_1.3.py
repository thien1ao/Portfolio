import matplotlib.pyplot as plt
import scipy.special
import random


w_list = []


def roll():
    return random.randint(1, 6)


def plot_(n):
    counter = 0

    for i in range(n):
        drfw = [roll() for _ in range(3)]
        if (drfw[0] < drfw[1] < drfw[2]):
            counter += 1

        w = counter / (i + 1)

        w_list.append(w)

        P = scipy.special.comb(6, 3) / 6 ** 3

        plt.plot(w_list, color="cornflowerblue")
        plt.axhline(y=P, color="orange")
        plt.grid(True)


plot_(1000)
plt.show()
