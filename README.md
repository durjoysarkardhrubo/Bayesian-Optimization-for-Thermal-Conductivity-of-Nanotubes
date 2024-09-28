# Bayesian-Optimization-for-Thermal-Conductivity-of-Nanotubes
This repository implements Bayesian Optimization using Gaussian Process Regression to predict the inner diameter of nanotubes for maximum and minimum thermal conductivity based on experimental data. The dataset includes eight inner diameters (in nm) and their corresponding thermal conductivity (in W/mK)
# Bayesian Optimization for Thermal Conductivity of Nanotubes

This repository uses **Bayesian Optimization** with **Gaussian Process Regression (GPR)** to predict the inner diameter of nanotubes that gives the maximum and minimum thermal conductivity. The code is based on a dataset containing eight inner diameter values and their corresponding thermal conductivity measurements. 

## Dataset:
- **Input (Inner Diameter in nm)**: 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0
- **Output (Thermal Conductivity in W/mK)**: 375, 450, 475, 510, 525, 515, 505, 495

![image](https://github.com/user-attachments/assets/bd5c577f-1fff-4f6d-8a70-79b417980248)


The script fits a Gaussian Process model to these data points and predicts the inner diameters that yield the maximum and minimum thermal conductivity.

## Requirements:
- Python 3.x
- scikit-learn
- numpy

You can install the required dependencies using:
```bash
pip install -r requirements.txt
