"""Python 3.14; NumPy/Matplotlib versions in root pyproject.toml.
Write the original PNG in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.6,3.9),layout='constrained',facecolor='white')
t=np.linspace(0,.5,601);mu=np.full_like(t,np.inf)
mu[:-1]=2*(1-t[:-1])/(1-2*t[:-1])**2
ax.fill_between(t,0,np.minimum(mu,12),color='#d3e9f3')
ax.axvspan(.5,1,color='#d3e9f3')
ax.plot(t,mu,color='#1e659b',lw=2)
ax.axvline(.5,color='#666666',ls='--',lw=1)
ax.text(.08,7.5,'unstable',color='#a33a32')
ax.text(.56,6.5,'unconditionally\nstable',color='#1e659b')
ax.text(.08,.7,'stable',color='#1e659b')
ax.set(xlim=(0,1),ylim=(0,12),xlabel='θ',ylabel='μ = κ Δt / (Δx)²',title='Mixed-width heat scheme: exact Fourier stability boundary')
ax.spines[['top','right']].set_visible(False)
fig.savefig('2010-heat-stability.png',dpi=155,facecolor='white')
