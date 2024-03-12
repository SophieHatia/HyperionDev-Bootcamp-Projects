
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

""" Exercise 3 """

i_deg = np.array([10,20,30,40,50,60,70,80])
i = i_deg*np.pi/180 # x
r_deg = np.array([8,15.5,22.5,29,35,40.5,45.5,50])
r = r_deg*np.pi/180 # y
sig_deg = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
sig = sig_deg*np.pi/180

matplotlib.rcParams["figure.figsize"] = [15,5]
matplotlib.rcParams.update({'font.size':12})
fig, (ax1,ax2,ax3) = plt.subplots(1,3)
xPlot = np.linspace(0, 2, 100)

M = [1,2,3]
for j in M:
    
    print("CASE",j)
    
    if j == 1:
        def ref(i, *params):
            [alpha] = params
            return alpha*i
        p0 = [1]
    if j == 2:
        def ref(i, *params):
            [alpha,beta] = params
            return alpha*i - beta*i**2
        p0 = [1,1]     
    if j == 3:
        def ref(i, *params):
            [ratio_ind] = params
            return np.arcsin(np.sin(i)/ratio_ind)
        p0 = [1]
        
    paramsHat, cov = curve_fit(ref, i, r, p0, sig, absolute_sigma=True)
    fit = ref(xPlot, *paramsHat)

    if j == 1 or j == 2:
        def deriv(i,n):
            der = [i,i**2]
            return der[n]
    if j == 3:
        def deriv(i,n):
            der = [np.cos(i)/(paramsHat[0]-np.sin(i)**2)]
            return der[n]
    
    sum2=[]
    for l in range(len(paramsHat)):  
        sum1=[]
        for k in range(len(paramsHat)):
            diff_l = deriv(xPlot,l)
            diff_k = deriv(xPlot,k)
            U_lk = cov[l,k]
            sum1.append(diff_l*diff_k*U_lk)              
        sum2.append(sum(sum1))
    sig_squared = sum(sum2) # this is sig of function
    
    chisq = sum(((r - ref(i, *paramsHat))/sig)**2) 
    n = len(r)-len(paramsHat)
    print(chisq,n)
    chi_per_n = chisq/n
    print("chi per n :",chi_per_n)   
    #chi_pdf = chi2.pdf(chisq,n)   
    pval = chi2.sf(chisq,n)
    print("pval :",pval)
    
    sig_params = np.sqrt(np.diag(cov)) # this is sig of params
    for l in range(len(paramsHat)):  
        for k in range(len(paramsHat)):
            U_lk = cov[l,k]
            sig_l = sig_params[l]
            sig_k = sig_params[k]
            rho = U_lk/(sig_l*sig_k)
            #print(l,k,cov[l,k],rho)
    
    if j == 1:
        ax1.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')
        ax1.errorbar(i, r, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax1.fill_between(xPlot, fit+np.sqrt(sig_squared), fit-np.sqrt(sig_squared))
        ax1.set_title("Hypothesis 1: Linear")
        ax1.set_xlabel(r'$i/rad$')
        ax1.set_ylabel(r'$r/rad$',)
        ax1.legend()
    if j == 2:
        ax2.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')
        ax2.errorbar(i, r, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax2.fill_between(xPlot, fit+np.sqrt(sig_squared), fit-np.sqrt(sig_squared))
        ax2.set_title("Hypothesis 2: Quadratic")
        ax2.set_xlabel(r'$i/rad$')
        ax2.set_ylabel(r'$r/rad$')
        ax2.legend()
    if j == 3:
        ax3.plot(xPlot, fit, 'orange', linewidth=2, label='fit result')       
        ax3.errorbar(i, r, yerr=sig, xerr=0, color='black', fmt='.', label='data')
        ax3.fill_between(xPlot, fit+np.sqrt(sig_squared), fit-np.sqrt(sig_squared))
        ax3.set_title("Ibn Sahl Relation")
        ax3.set_xlabel(r'$i/rad$')
        ax3.set_ylabel(r'$r/rad$')
        ax3.legend()