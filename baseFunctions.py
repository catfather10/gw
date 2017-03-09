from scipy import integrate
import numpy as np
from numpy.random import random as rng
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

####stałe
H_0=70.4 # km/s  Mpc^-1
Omega_m=0.27 
Omega_lambda=1-Omega_m
c=299792 # km/s
D_H=c/H_0

    
def E(z): # z = redshift
    return np.sqrt(Omega_m*(1+z)**3+(1-Omega_m))
    
def D_c(z):
    z2=lambda z: 1/E(z)
    return D_H*integrate.quad(z2,0,z)[0]  
def D_L(z):
    return (1+z)*D_c(z)
    
def z_max(A,m):
    toSolve = lambda z:A*(m*(1+z)**(5/6))/D_L(z)-2
    return fsolve(toSolve,.1)[0]
    
def z_from_Dl(Dl):
    toSolve = lambda z : Dl- D_L(z) 
    return fsolve(toSolve,.1)
    
def D_T(z):
    z2=lambda z: 1/(E(z)*(1+z))
    return D_H*integrate.quad(z2,0,z)[0]

def z_from_DT(DT):
    toSolve = lambda z : DT- D_T(z) 
    return fsolve(toSolve,.1)
    
def DNSDistribution_z(z,mergerRateFun): ### dN/dz
    return mergerRateFun(z)/(1+z)*4*np.pi*D_c(z)**2*D_H/E(z)
    
def SNR(Dl,theta,phi,psi,iota,m,A):
    FP=0.5*(1+(np.cos(theta))**2)*np.cos(2*phi)*np.cos(2*psi)-np.cos(theta)*np.sin(2*phi)*np.sin(2*psi)
    FX=0.5*(1+(np.cos(theta))**2)*np.cos(2*phi)*np.sin(2*psi)+np.cos(theta)*np.sin(2*phi)*np.cos(2*psi)
    TH=2*np.sqrt(((FP*(1+(np.cos(iota))**2))**2) +4*(FX*np.cos(iota))**2) 
    return A*TH*m**(5/6)/Dl
    
def MonteCarloProb(probFun,xRange,yRange):
    k=0
    while (True):
        k+=1
        x=rng()*(xRange[1]-xRange[0])+xRange[0]
        y=rng()*(yRange[1]-yRange[0])+yRange[0]
        if(probFun(x)>y):
#            return k
#            print(k) #### !!!!!!!!!!!!
            return x
            
def plotAndSave(name,xs,ys,xLab,yLab,LogLog=False,saveName=0,xrange=-1):
    plt.xlabel(xLab)
    plt.ylabel(yLab)
    if(LogLog):
        name+=" LogLog"
    plt.title(name)
    plt.plot(xs,ys)
    if(saveName!=0):
        name=saveName
    if (LogLog):
        plt.xscale('log')
        plt.yscale('log')
        name+="_LogLog"
    plt.savefig("pics/v2/"+name+".png",dpi=150)
    
def V_c(z):
    return 4*np.pi*D_c(z)**2*D_H/E(z)
    

      
#m=1
#toSolve= lambda z: SNR(D_L(z),)
#t=fsolve(toSolve,.1)
#print(t)
#print(z_max())

   
   
### testy Gestosc prawdopodobienstwa        
#print(z_max())
#xs=np.linspace(0, z_max(), num=100)
#ys=DNSProb_z_vector(xs)
##plotAndSave("Gestosc prawdopodobienstwa",xs,ys,"redshift","dP/dz",saveName="ProbDens_z")
##plotAndSave("Gestosc prawdopodobienstwa",xs,ys,"redshift","dP/dz",LogLog=True,saveName="ProbDens_z")
#plotAndSave("Gestosc prawdopodobienstwa_Dhorizon=10Gpc",xs,ys,"redshift","dP/dz",saveName="ProbDens_z_Dhorizon=10Gpc")
#plotAndSave("Gestosc prawdopodobienstwa_Dhorizon=10Gpc",xs,ys,"redshift","dP/dz",LogLog=True,saveName="ProbDens_z_Dhorizon=10Gpc")
#fitFun =lambda x,a: a*x**2 
#popt, pcov = curve_fit(f=fitFun, xdata=xs, ydata=ys,p0=(1))
#print(popt)
#print(np.sqrt(np.diag(pcov)))

