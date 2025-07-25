import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

lambdas = [0.25, 0.5, 0.75, 1.0, 2.0]

rand_arr = np.sort(np.random.uniform(low=0, high=1, size=10000))

res = np.diff(rand_arr)

sns.histplot(data=res, kde=True, bins=50, stat="density", color="cornflowerblue",
             line_kws={'linestyle': 'dashed', 'linewidth': 2},
             ).lines[0].set_color('orange')

plt.grid(True)
plt.show()

x = np.linspace(0, 5, 500)

for lam in lambdas:
    y = lam * np.exp(-lam * x)
    plt.plot(x, y, label=f"(λ={lam})")

plt.legend()
plt.grid(True)
plt.show()
