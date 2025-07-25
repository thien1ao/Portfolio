import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

n = 100
p = 1/6
sechs_list = np.arange(0, 100)

pmf = scipy.stats.binom.pmf(sechs_list, n, p)


plt.bar(sechs_list, pmf, color='cornflowerblue')

plt.fill_between(sechs_list[sechs_list > 20], pmf[sechs_list > 20], color='orange', label='P(X > 20)')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
