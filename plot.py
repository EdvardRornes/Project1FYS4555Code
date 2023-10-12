# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:30:18 2023

@author: edvar
"""

import matplotlib.pyplot as plt
import numpy as np

#cosθ
c = np.arange(-0.99,0.99,0.001)
#√s
s = np.arange(0.1,30,0.001)
#SI-conversion factor
SI_con = 3.893*10**-4

#Constants (in this problem)
alpha = 1/137
E = 14
prefactor = alpha**2/(2*E**2)

#Various differential cross section terms
def uchan(c):
    return SI_con*10**9*prefactor*((1+c)**2+4)/(1-c)**2
def schan(c):
    return SI_con*10**9*prefactor*1/2*(1+c**2)
#Interference term
def ichan(c):
    return SI_con*10**9*prefactor*(1+c)**2/(1-c)

#Differential cross section terms summed
def dcs(c):
    return (uchan(c)+schan(c)-ichan(c))

#Total cross section
def tcs(s):
    return 10**6*737*SI_con*np.pi*alpha**2/(2*s**2)

#Plot style
plt.style.use("ggplot")

# Summed cross section terms plotted
plt.plot(c,dcs(c),"b", label="Sum")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.xlim(-1,1)
plt.xlabel("cosθ")
plt.ylabel("dσ/dΩ [nb/sr]")
plt.yscale("log")
plt.show()

# Individual cross section terms plotted
plt.plot(c,dcs(c),"b", label="Sum")
plt.plot(c,uchan(c),"g", label="Scattering")
plt.plot(c,schan(c),"y", label="Annihilation")
plt.plot(c,ichan(c),"r", label="Interference")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Differential Cross Section")
plt.xlim(-1,1)
plt.xlabel("cosθ")
plt.legend(loc="upper left")
plt.ylabel("dσ/dΩ [nb/sr]")
plt.yscale("log")
plt.show()

# s-channel term plotted
plt.plot(c,schan(c),"y", label="Annihilation")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Annihilation Channel")
plt.xlim(-1,1)
plt.xlabel("cosθ")
plt.ylabel("dσ/dΩ [nb/sr]")
plt.show()

# Total differential cross section plotted
plt.plot(s,tcs(s),"b", label="Sum")
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.title("Total Cross Section")
plt.xlim(-1,31)
plt.xlabel("√s [GeV]")
plt.ylabel("σ [μb]")
plt.yscale("log")
plt.show()