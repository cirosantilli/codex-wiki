"""Original teaching plot. Python3.14,NumPy2.3.5,Matplotlib3.10.7. PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

x=np.linspace(-3,3,500);terrain=.35*np.exp(-x*x/.7);upper=np.ones_like(x)
fig,(a,b)=plt.subplots(2,1,figsize=(7.5,5.5),layout='constrained',sharex=True,gridspec_kw={'height_ratios':[1.3,1]})
a.fill_between(x,0,terrain,color='#baaa87');a.plot(x,terrain,color='#74634c',lw=1.5);a.plot(x,upper,color='.35',lw=2)
a.fill_between(x,terrain,upper,color='#d9eaf3');a.axhline(1,color='.35',lw=1.3)
for xx in [-2.5,0]:
 hh=.35*np.exp(-xx*xx/.7);a.annotate('',(xx,1),(xx,hh),arrowprops={'arrowstyle':'<->','color':'#1e5779'})
a.annotate('Crossing flow',(1.3,1.14),(-1.3,1.14),ha='center',va='center',arrowprops={'arrowstyle':'->','color':'.3'})
a.text(1.6,.7,'Fixed upper boundary',fontsize=10);a.set(ylim=(0,1.3),ylabel='Layer height / H',title='Idealized layer compression over terrain')
b.plot(x,-terrain,color='#2b688c',lw=2.5);b.axhline(0,color='.5',lw=.8);b.set(xlabel='Horizontal coordinate (schematic)',ylabel=r'$\zeta/f_0$',ylim=(-.4,.035));b.text(0,-.12,'Anticyclonic tendency',ha='center',fontsize=10);b.grid(alpha=.13)
fig.savefig(Path(__file__).stem+'.png',dpi=150,facecolor='white');plt.close(fig)
