from utils import load_data, dL
import numpy as np

data = load_data()
z = data["z"].values

H0, Om, alpha = 70, 0.23, -0.05

mu_model = np.array([5*np.log10(dL(zi, H0, Om, alpha)) + 25 for zi in z])

print("Background Expansion computed")
