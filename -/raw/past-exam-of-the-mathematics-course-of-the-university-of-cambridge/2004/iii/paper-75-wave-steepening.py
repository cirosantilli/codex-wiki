"""Original sketch. Tested with Python 3.14, numpy 2.3, matplotlib 3.10.
Writes only its opaque PNG basename in the caller's current directory.
The caller may supply MPLCONFIGDIR; this script preserves it.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})
fig,ax=plt.subplots(1,4,figsize=(13.5,3.7),layout='constrained',facecolor='white')
a=.2
T=2/(3*a)
for s in np.linspace(0,1.5,11):
    t=np.linspace(s,T,150)
    ax[0].plot((1+1.5*a*np.sin(s))*(t-s),t,color=plt.cm.viridis(s/1.5))
ax[0].plot([0,T],[0,T],'k--',lw=1.4,label='leading edge')
ax[0].plot(T,T,'ro',label='first intersection')
ax[0].set(xlabel=r'$x\omega/c_0$',ylabel=r'$\omega t$',title='Outgoing characteristics')
ax[0].legend(fontsize=8,loc='upper left')
for j,t in enumerate([1,2.7]):
    s=np.linspace(0,t,900)
    x=(1+1.5*a*np.sin(s))*(t-s)
    h=(1+.5*a*np.sin(s))**2
    ax[j+1].plot(x,h,color=['#1469a0','#b24716'][j],lw=2)
    ax[j+1].plot([t,t+.7],[1,1],color='gray')
    ax[j+1].axhline(1,color='gray',lw=.7,ls=':')
    ax[j+1].set(xlabel=r'$x\omega/c_0$',ylabel=r'$h/H$',title=rf'Profile at $\omega t={t:g}$',ylim=(.97,1.24))
    ax[j+1].text(.03,.94,'Forward slope steepens',transform=ax[j+1].transAxes,va='top',fontsize=9)
ax[3].plot([0,.5,.9,1.25,1.45,1.45,1.9],[1.07,1.16,1.21,1.17,1.11,1,1],color='#b24716',lw=2)
ax[3].axhline(1,color='gray',ls=':',lw=.7)
ax[3].annotate('Bore',xy=(1.45,1.05),xytext=(.5,1.04),arrowprops={'arrowstyle':'->'})
ax[3].set(xlabel='Distance (schematic)',ylabel=r'$h/H$',title='After smooth-wave failure',ylim=(.97,1.24))
ax[3].set_xticks([])
fig.savefig('paper-75-wave-steepening.png',dpi=120,facecolor='white',transparent=False)
