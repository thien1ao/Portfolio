import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu_m = 170
sigma_m = 9
mu_w = 160
sigma_w = 8

delta_mu = mu_m - mu_w
delta_sigma = np.sqrt(sigma_w**2 + sigma_m**2)


x = np.linspace(150, 200, 1000)

pdf_val_m = norm.pdf(x, mu_m, sigma_m)
pdf_val_w = norm.pdf(x, mu_w, sigma_w)


P = norm.cdf(0, delta_mu, delta_sigma)

plt.plot(x, pdf_val_m, color='cornflowerblue', label="Männer")
plt.plot(x, pdf_val_w, color="orange", label="Frauen")
plt.axhline(color="white", label=f"P={P:.2f}")
plt.legend()
plt.grid(True)
plt.show()
