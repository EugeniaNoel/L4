import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

#Los datos
variable_x = np.array([0, 1, 2, 3, 4])
variable_y = np.array([0, 2, 4, 6, 8])

#La funcion que quiero ajustar
g = lambda x, a, b: a*x+b

#Realizo el ajuste
popt_g, pcov_g  = curve_fit(g, variable_x, variable_y)
sigmas_g     = [pcov_g[0,0], pcov_g[1,1]]

#Calculo el R^2 del ajuste
residuals = variable_y- g(variable_x, popt_g[0], popt_g[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((variable_y-np.mean(variable_y))**2)
r_squared = 1 - (ss_res / ss_tot)

print('parametros optimos: ', popt_g, '\n desviaciones estandar: ', np.sqrt(sigmas_g), '\n R^2: ',r_squared)

#Grafico
plt.plot(variable_x, variable_y, label='datos')
plt.plot(variable_x, g(variable_x, popt_g[0], popt_g[1]), label='ajuste')
plt.legend()