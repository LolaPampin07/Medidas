# -*- coding: utf-8 -*-
# %%Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Importe de datos archivo csv
data = pd.read_csv('TPIMPEDANCIA.csv', delimiter=';')
lnR = data['lnR'].values
invT = data['invT_K'].values
# %% Calculo
# Creo matriz
X = np.column_stack((np.ones_like(lnR), lnR, lnR**3))
# Ajuste por mínimos cuadrados
coeffs, _, _, _ = np.linalg.lstsq(X, invT, rcond=None)
A, B, C = coeffs
# %% Graficos
print(f"Coeficientes Steinhart-Hart:\nA = {A:.6e}\nB = {B:.6e}\nC = {C:.6e}")
# Generar curva ajustada
lnR_fit = np.linspace(min(lnR), max(lnR), 500)
invT_fit = A + B * lnR_fit + C * lnR_fit**3
T_fit = 1 / invT_fit#
plt.figure(figsize=(8, 6))
plt.plot(1 / invT, np.exp(lnR),'x', color='orange', label='Datos')
plt.plot(T_fit, np.exp(lnR_fit), color='red', linewidth=2, label='Ajuste Steinhart-Hart')
plt.xlabel('Temperatura (K)')
plt.ylabel('Resistencia (Ohm)')
plt.title('Ajuste Steinhart-Hart')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
