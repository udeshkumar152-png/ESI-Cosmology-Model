from utils import load_data, dL
import matplotlib.pyplot as plt
import numpy as np

data = load_data()

z = data["z"].values
mu_obs = data["mu"].values
sigma = data["mu_err"].values

H0, Om, alpha = 70, 0.23, -0.05

mu_model = np.array([5*np.log10(dL(zi, H0, Om, alpha)) + 25 for zi in z])

residual = (mu_obs - mu_model)/sigma

plt.scatter(z, residual)
plt.axhline(0)
plt.show()
