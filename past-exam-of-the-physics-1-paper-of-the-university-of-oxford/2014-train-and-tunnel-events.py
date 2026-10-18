"""Original spacetime plots. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes only 2014-train-and-tunnel-events.png in the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=.99;g=1/np.sqrt(1-b*b);L=100/g;ctB=(90-L)/b;ctpB=g*(ctB-b*90)
fig,axs=plt.subplots(1,2,figsize=(10.7,5),facecolor='white')
t=np.linspace(-30,130,400);a=axs[0]
a.plot(np.zeros_like(t),t,color='#263849',label='Tunnel portals');a.plot(np.full_like(t,90),t,color='#263849')
a.plot(b*t,t,color='#b14c29',label='Train ends');a.plot(b*t+L,t,color='#b14c29')
a.axhline(40,color='#236b8e',ls=':',lw=1.5)
a.plot([40*b,40*b+L],[40,40],lw=7,color='#b14c29',alpha=.65)
a.text(9,45,'Simultaneous train: 14.11 m',color='#236b8e',fontsize=9)
a.scatter([0,90],[0,ctB],c='black',zorder=5);a.annotate('A: rear enters',(0,0),xytext=(6,-19),fontsize=9);a.annotate('B: front leaves',(90,ctB),xytext=(95,80),fontsize=9)
a.set(xlim=(-30,150),ylim=(-30,130),xlabel='x (m)',ylabel='ct (m)',title='Track frame: A precedes B');a.legend(loc='upper left',fontsize=9)
t=np.linspace(-120,70,400);a=axs[1]
a.plot(-b*t,t,color='#263849',label='Tunnel portals');a.plot(90/g-b*t,t,color='#263849')
a.plot(np.zeros_like(t),t,color='#b14c29',label='Train ends');a.plot(np.full_like(t,100),t,color='#b14c29')
a.axhline(-40,color='#236b8e',ls=':',lw=1.5)
a.plot([40*b,90/g+40*b],[-40,-40],lw=7,color='#263849',alpha=.65)
a.text(3,-29,'Simultaneous tunnel: 12.70 m',color='#236b8e',fontsize=9)
a.scatter([0,100],[0,ctpB],c='black',zorder=5);a.annotate('A: rear enters',(0,0),xytext=(8,8),fontsize=9);a.annotate('B: front leaves',(100,ctpB),xytext=(65,-107),fontsize=9)
a.set(xlim=(-30,150),ylim=(-120,70),xlabel="x′ (m)",ylabel="ct′ (m)",title='Train frame: B precedes A');a.legend(loc='upper right',fontsize=9)
for a in axs:a.grid(alpha=.16);a.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path('2014-train-and-tunnel-events.png'),dpi=140,facecolor='white')
