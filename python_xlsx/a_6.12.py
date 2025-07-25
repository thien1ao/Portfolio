import matplotlib.pyplot as plt
import numpy as np

gesunde_apf = np.zeros(550 - 11)
faule_apf = np.ones(11)
haufen = np.concatenate((gesunde_apf, faule_apf))

stichprobe = 25

simulation_number = 10000

faul_counter = []

res = []
counter = 0

for i in range(simulation_number):
    random_choice = np.random.choice(haufen, stichprobe, replace=False)

    if np.sum(random_choice) == 2:
        counter += 1

    res.append(counter/(i+1))

p = counter/simulation_number

plt.plot(res, color="cornflowerblue")
plt.axhline(y=p, color="orange", label=f"P: {p:.2f}")
plt.legend()
plt.grid(True)
plt.show()
