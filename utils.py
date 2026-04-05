import numpy as np
import pandas as pd

# LOAD DATA
def load_data():
    data = pd.read_csv(
        "data/desi_data.txt",
        delim_whitespace=True,
        comment="#",
        header=None
    )
    data.columns = ["SN", "z", "mu", "mu_err", "extra"]
    return data

# MODEL
c = 299792.458

def H(z, H0, Om, alpha):
    return H0 * np.sqrt(Om*(1+z)**3 + (1-Om)*(1 + alpha*np.log(1+z)))

def dL(z, H0, Om, alpha):
    z_arr = np.linspace(0, z, 200)
    dz = z / 200
    integral = np.sum(1/H(z_arr, H0, Om, alpha)) * dz
    return (1+z) * c * integral
