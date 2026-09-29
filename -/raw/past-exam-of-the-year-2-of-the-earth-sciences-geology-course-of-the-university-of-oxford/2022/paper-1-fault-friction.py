"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

fig,axes=plt.subplots(1,2,figsize=(7.6,3.3),dpi=100)
for ax,dip in zip(axes,[65,55]):
    phi=np.deg2rad(2*dip-90);mu=np.tan(phi)
    ratio=(1+np.sin(phi))/(1-np.sin(phi));C=(ratio+1)/2;R=(ratio-1)/2
    th=np.linspace(0,np.pi,600)
    ax.plot(C+R*np.cos(th),R*np.sin(th),color='#344654',lw=2,label='effective-stress circle')
    xx=np.linspace(0,ratio+.3,100)
    ax.plot(xx,mu*xx,color='#b44b26',lw=1.8,label='frictional failure envelope')
    sx=C*np.cos(phi)**2;sy=C*np.sin(phi)*np.cos(phi)
    assert np.isclose(sy/sx,mu)
    ax.plot(sx,sy,'o',color='#177ca4')
    ax.plot([C,sx],[0,sy],':',color='#177ca4')
    ax.set(xlim=(0,ratio+.35),ylim=(0,R*1.25+.1),xlabel="Effective normal stress σ′ₙ",ylabel='Shear stress τ')
    ax.set_title(f'Dip {dip}°, φ = {2*dip-90}°, μ = {mu:.3f}',fontsize=11)
    ax.grid(color='#e4e9ed',lw=.6)
    ax.set_aspect('equal',adjustable='box')
fig.legend(*axes[0].get_legend_handles_labels(), loc='lower center', ncol=2, frameon=False, fontsize=9)
fig.tight_layout(rect=(0,.12,1,1),pad=1.0,w_pad=2)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
