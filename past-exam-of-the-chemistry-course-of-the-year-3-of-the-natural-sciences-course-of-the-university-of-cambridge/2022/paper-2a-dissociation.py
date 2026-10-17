"""Original solution figure. Tested with Python 3.14, numpy and matplotlib.
The PNG basename is written to the current working directory for Make's _media target.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, flow, finish, save

nu=np.array([56298.9,56628.2,56924.2,57185.9,57412.6,57603.3]);x=np.arange(5)+.5;spacing=np.diff(nu);b,a=np.polyfit(x,spacing,1);root=-a/b;limit=nu[0]-a*a/(2*b)
fig,axs=plt.subplots(1,2,figsize=(10,4.3))
a0=axs[0];xx=np.linspace(0,root,250);yy=a+b*xx;a0.plot(xx,yy,color='#245c9f',label='linear spacing fit');a0.scatter(x,spacing,color='#b45309',label='successive differences',zorder=3);a0.fill_between(xx,0,yy,color='#245c9f',alpha=.12);a0.axhline(0,color='.5',lw=.7);a0.set(xlabel='Relative midpoint index n + ½',ylabel=r'Spacing / cm$^{-1}$',title='Remaining energy from an extrapolated area');a0.legend(fontsize=9);a0.text(5,180,'Area ≈ 1743 cm⁻¹',ha='center',fontsize=11)
a1=axs[1];n=np.linspace(0,root,200);a1.plot(n,nu[0]+a*n+.5*b*n*n,color='#245c9f');a1.scatter(np.arange(6),nu,color='#b45309',zorder=3);a1.axhline(limit,ls='--',color='.5');a1.text(2,limit-100,f'Estimated limit ≈ {limit:.0f} cm⁻¹',fontsize=10);a1.set(xlabel='Relative level index n',ylabel=r'Transition wavenumber / cm$^{-1}$',title='Quadratic progression implied by the spacing fit');a1.ticklabel_format(axis='y',style='plain',useOffset=False)
fig.tight_layout();save(fig,'paper-2a-dissociation.png')
