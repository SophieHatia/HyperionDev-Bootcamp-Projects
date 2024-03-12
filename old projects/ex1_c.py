import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x   = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y   = np.array([2.7, 3.9, 5.5, 5.8, 6.5, 6.3, 7.7, 8.5, 8.7])
sig = np.array([0.3, 0.5, 0.7, 0.6, 0.4, 0.3, 0.7, 0.8, 0.5])
xPlot=np.linspace(0,20,100)


matplotlib.rcParams["figure.figsize"] = [15,5]
matplotlib.rcParams.update({'font.size':12})
fig, (ax1,ax2, ax3) = plt.subplots(1,3)
#xPlot = np.linspace(0, 20, 100)

p0 = np.array([1,1,1,1])
def poly(x, *theta):
    [theta0,theta1,theta2,theta3]=theta
    return theta0+theta1*x+theta2*x**2+theta3*x**3

thetaHat,cov = curve_fit(poly,x,y,p0,sig,absolute_sigma=True)
fit=poly(xPlot,*thetaHat)

a=5
b=[6, 10, 20]
for i in b:
    print("Case",i)
    
    def delAB(a,b, *thetaHat):
        return poly(a,*thetaHat)-poly(b,*thetaHat)
    
    def deriv(n,a,b):
        der=[0,a-b,(a**2)-(b**2),(a**3)-(b**3)]
        return der[n]
    sum2=[]
    for j in range(len(thetaHat)):
        sum1=[]
        for k in range(len(thetaHat)):
            diff_j = deriv(j,5,i)
            diff_k = deriv(k,5,i)
            U_jk = cov[j,k]
            sum1.append(diff_j*diff_k*U_jk)
        sum2.append(sum(sum1))
    sig_poly_squared = sum(sum2)
    
    print(sig_poly_squared)
    
    if i==6:
        ax1.plot(xPlot, fit, 'red', linewidth=2, label='fit result')
        ax1.errorbar(x,y,yerr=sig,xerr=0,color='black',fmt='0', label='data')
        ax1.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax1.set_title("a=5,b=6")
        ax1.set_xlabel(r'$x$')
        ax1.set_ylabel(r'$y$')
        ax1.legend=()
    if i==10:
        ax2.plot(xPlot, fit, 'red', linewidth=2, label='fit result')
        ax2.errorbar(x,y,yerr=sig,xerr=0,color='black',fmt='0', label='data')
        ax2.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax2.set_title("a=5,b=10")
        ax2.set_xlabel(r'$x$')
        ax2.set_ylabel(r'$y$')
        ax2.legend=()
    if i==20:
        ax3.plot(xPlot, fit, 'red', linewidth=2, label='fit result')
        ax3.errorbar(x,y,yerr=sig,xerr=0,color='black',fmt='0', label='data')
        ax3.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        ax3.set_title("a=5,b=20")
        ax3.set_xlabel(r'$x$')
        ax3.set_ylabel(r'$y$')
        ax3.legend=()
        