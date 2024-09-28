import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern

# Input diameters (nm)
X = np.array([[1.5], [3.0], [4.5], [6.0], [7.5], [9.0], [10.5], [12.0]])

# Corresponding thermal conductivity (W/mK)
Y = np.array([375, 450, 475, 510, 525, 515, 505, 495])

# GP model with Matern kernel
kernel = Matern(nu=2.5)
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Fit model
gp.fit(X, Y)

# New diameters to predict
X_new = np.linspace(1.5, 12.0, 100).reshape(-1, 1)

# Predict
Y_pred, sigma = gp.predict(X_new, return_std=True)

# Find max and min
max_index = np.argmax(Y_pred)
min_index = np.argmin(Y_pred)
optimal_diameter_max = X_new[max_index]
optimal_diameter_min = X_new[min_index]

print(f"Maximum thermal conductivity at inner diameter: {optimal_diameter_max[0]:.2f} nm")
print(f"Minimum thermal conductivity at inner diameter: {optimal_diameter_min[0]:.2f} nm")
