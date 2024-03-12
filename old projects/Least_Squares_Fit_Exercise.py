import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x   = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y   = np.array([2.7, 3.9, 5.5, 5.8, 6.5, 6.3, 7.7, 8.5, 8.7])
sig = np.array([0.3, 0.5, 0.7, 0.6, 0.4, 0.3, 0.7, 0.8, 0.5])
xPlot=np.linspace(0,20,100)

m = [1,2,3]
for i in m:
    
    if i==1:
        def pol(x, *theta):
            [theta0,theta1]=theta
            return theta0+theta1*x
    if i==2:
        def pol(x,*theta):
            [theta0,theta1,theta2]=theta
            return theta0 + theta1*x +theta2*(x**2)
    if i==3:
        def pol(x,*theta):
            [theta0,theta1,theta2,theta3]=theta
            return theta0 + theta1*x + theta2*(x**2) + theta3*(x**3)
        
    p0=[]
    for j in range(i+1):
        p0.append(1)
        
    thetaHat, cov = curve_fit(pol, x, y, p0, sig, absolute_sigma=True)   
    chisq = sum(((y - pol(x, *thetaHat))/sig)**2)
    fit = pol(xPlot,*thetaHat)
    
    def deriv(x,n):
        der = [1, x, x**2, x**3]
        return der[n]
    sum2=[]
    for j in range(len(thetaHat)):
        sum1=[]
        for k in range(len(thetaHat)):
            diff_j = deriv(xPlot, j)
            diff_k = deriv(xPlot, k)
            U_jk = cov[j,k]
            sum1.append(diff_j*diff_k*U_jk)
            sum2.append(sum(sum1))
    sig_poly_squared = sum(sum2)        
       
   


    if i == 1:
        fig, ax = plt.subplots(1,1)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.15)
        plt.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='o', label='data')
        plt.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        plt.title("M=1")
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$', labelpad=10)        
        fit = pol(xPlot, *thetaHat)
        plt.plot(xPlot, fit, 'red', linewidth=2, label='fit result')     
#    plt.savefig("Least_Squares_Fit_1.pdf", format='pdf')
        plt.show()
    
    if i==2:
        fig, ax = plt.subplots(1,1)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.15)
        plt.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='o', label='data')
        plt.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))
        plt.title("M=2")
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$', labelpad=10)
#    xPlot = np.linspace(0, 10, 100)        
        fit = pol(xPlot, *thetaHat)
        plt.plot(xPlot, fit, 'red', linewidth=2, label='fit result')     
#    plt.savefig("Least_Squares_Fit_2.pdf", format='pdf')
        plt.show()  
    
    if i==3:
        fig, ax = plt.subplots(1,1)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.15)
        plt.errorbar(x, y, yerr=sig, xerr=0, color='black', fmt='o', label='data')
        plt.fill_between(xPlot, fit+np.sqrt(sig_poly_squared), fit-np.sqrt(sig_poly_squared))        
        plt.title("M=3")
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$', labelpad=10)
        #    xPlot = np.linspace(0, 10, 100)        
        fit = pol(xPlot, *thetaHat)
        plt.plot(xPlot, fit, 'red', linewidth=2, label='fit result')     
        #    plt.savefig("Least_Squares_Fit_3.pdf", format='pdf')
        
        plt.show()
            
        


