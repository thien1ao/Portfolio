import numpy as np
import matplotlib.pyplot as plt


schlaue = np.full(3, 1)
andere = np.full(15-len(schlaue), 0)
simulation = 10000

schlau_pro_klass = 0
drei_schlau = 0

res_1_pro_kl = []
res_3_pro_kl = []

for i in range(simulation):
    studenten = np.concatenate((schlaue, andere))
    np.random.shuffle(studenten)

    classes = np.array_split(studenten, 3)

    schlau_counter = [np.sum(cls) for cls in classes]

    if schlau_counter.count(1) == 3:
        schlau_pro_klass += 1

    if 3 in schlau_counter:
        drei_schlau += 1

    res_1_pro_kl.append(schlau_pro_klass/(i+1))
    res_3_pro_kl.append(drei_schlau/(i+1))

w1 = schlau_pro_klass / simulation
w2 = drei_schlau / simulation

plt.plot(res_1_pro_kl, color="cornflowerblue", label="1 pro Klasse")
plt.plot(res_3_pro_kl, color="blue", label="3 in einer Klasse")
plt.axhline(y=w1, color="orange", label=f"P1: {w1:.2f}")
plt.axhline(y=w2, color="coral", label=f"P1: {w2:.2f}")
plt.legend()
plt.grid(True)
plt.show()
