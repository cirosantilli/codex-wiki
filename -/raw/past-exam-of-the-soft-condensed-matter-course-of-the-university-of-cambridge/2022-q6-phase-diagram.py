"""Original qualitative phase diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Curves are illustrative, not fitted or computed coexistence data. Output is in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':10, 'figure.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(9.2,4.2),layout='constrained')
y=np.linspace(0,3,250)
eta_f=.49/(1+.52*y)**2
eta_s=.55/(1+.52*y)**2
for ax in axs:
    ax.fill_betweenx(y,0,eta_f,color='#e1f2fd')
    ax.fill_betweenx(y,eta_f,eta_s,color='#f8ecc9')
    ax.fill_betweenx(y,eta_s,.64,color='#e5eee2')
    ax.plot(eta_f,y,color='#2f6d8c',lw=1.8)
    ax.plot(eta_s,y,color='#4d7b41',lw=1.8)
    ax.set(xlim=(0,.64),ylim=(0,3),xlabel=r'Particle volume fraction $\eta$',ylabel=r'Screening length $\lambda_D/a$ (schematic)')
    ax.set_yticks([])
    ax.spines[['top','right']].set_visible(False)
    ax.text(.035,.65,'fluid',color='#2f6d8c')
    ax.text(.43,2.4,'crystal',color='#4d7b41')
    ax.text(.27,.4,'fluid + crystal',rotation=52,fontsize=9,color='#776126')
axs[0].annotate('add salt',xy=(.25,.30),xytext=(.25,2.3),ha='center',arrowprops={'arrowstyle':'->','ls':'--','color':'#8a3e73'},color='#8a3e73')
axs[0].set_title('Fixed charge: salt decreases screening length')
eta_f_high=.49/(1+.75*y)**2
eta_s_high=.55/(1+.75*y)**2
axs[1].plot(eta_f_high,y,'--',color='#a33f48',lw=1.6,label='higher surface charge')
axs[1].plot(eta_s_high,y,'--',color='#a33f48',lw=1.6)
axs[1].annotate('',xy=(eta_f_high[100],y[100]),xytext=(eta_f[100],y[100]),arrowprops={'arrowstyle':'->','color':'#a33f48'})
axs[1].legend(loc='lower left',bbox_to_anchor=(0,1.0),frameon=False,fontsize=9)
axs[1].set_title('Stronger charge shifts freezing to lower density',pad=32)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
