import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

""" Exercises 1a and 1b """

x   = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y   = np.array([2.7, 3.9, 5.5, 5.8, 6.5, 6.3, 7.7, 8.5, 8.7])
sig = np.array([0.3, 0.5, 0.7, 0.6, 0.4, 0.3, 0.7, 0.8, 0.5])

matplotlib.rcParams["figure.figsize"] = [15,5]
matplotlib.rcParams.update({'font.size':12})
fig, (ax1,ax2,ax3) = plt.subplots(1,3)
xPlot = np.linspace(0, 20, 100)

M = [1,2,3]
for i in M:
    
 #   print("CASE",i)
    
    if i == 1:
        def poly(x, *theta):
            [theta0,theta1] = theta
            return theta0 + theta1*x
    if i == 2:
        def poly(x, *theta):
            [theta0,theta1,theta2] = theta
            return theta0 + theta1*x + theta2*x**2
    if i == 3:
        def poly(x, *theta):
            [theta0,theta1,theta2,theta3] = theta
            return theta0 + theta1*x + theta2*x**2 + theta3*x**3 
        
    p0 = []
    for j in range(i+1):
        p0.append(1)
    
    thetaHat, cov = curve_fit(poly, x, y, p0, sig, absolute_sigma=True)
    fit = poly(xPlot, *thetaHat)
    
    def deriv(x,n):       
        der = [1, x, x**2, x**3]
        return der[n]    
    sum2=[]
    for j in range(len(thetaHat)):  
        sum1=[]
        for k in range(len(thetaHat)):
            diff_j = deriv(xPlot,j)
            diff_k = deriv(xPlot,k)
            U_jk = cov[j,k]
            sum1.append(diff_j*diff_k*U_jk)              
        sum2.append(sum(sum1))
    sig_poly_squared = sum(sum2)
    
     
    if i == 1:
        ax1.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')
        ax1.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax1.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax1.set_title("First Order Polynomial")
        ax1.set_xlabel(r'$x$')
        ax1.set_ylabel(r'$y$',)
        ax1.legend()
    if i == 2:
        ax2.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')
        ax2.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax2.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax2.set_title("Second Order Polynomial")
        ax2.set_xlabel(r'$x$')
        ax2.set_ylabel(r'$y$')
        ax2.legend()
    if i == 3:
        ax3.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')
        ax3.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax3.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax3.set_title("Third Order Polynomial")
        ax3.set_xlabel(r'$x$')
        ax3.set_ylabel(r'$y$')
        ax3.legend()
