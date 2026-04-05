from utils import load_data, dL
import numpy as np

data = load_data()

z = data["z"].values
mu_obs = data["mu"].values
sigma = data["mu_err"].values

best_chi2 = 1e10
best_params = None

for H0 in [66, 67, 68]:
    for Om in [0.2, 0.23, 0.26]:
        for alpha in [-0.1, -0.05, 0]:

            mu_model = np.array([
                5*np.log10(dL(zi, H0, Om, alpha)) + 25
                for zi in z
            ])

            chi2 = np.sum(((mu_obs - mu_model)/sigma)**2)

            if chi2 < best_chi2:
                best_chi2 = chi2
                best_params = (H0, Om, alpha)

print("Best Params =", best_params)
