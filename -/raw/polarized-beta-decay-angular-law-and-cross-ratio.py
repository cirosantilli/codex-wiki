"""Original chosen angular law and spin-reversal count example, not historical data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media to emit basename.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
a = -.3
u = np.linspace(-1, 1, 401)
pdf = (1+a*u)/2
blue, red = '#176a9c', '#b44829'
fig = plt.figure(figsize=(13.5, 6.5), facecolor='white')
gs = fig.add_gridspec(2, 2, width_ratios=[1.05, 1.05], height_ratios=[1, .46],
                      left=.07, right=.97, bottom=.21, top=.80, hspace=.35, wspace=.25)
ax = fig.add_subplot(gs[:, 0])
ax.plot(u, pdf, color=blue, lw=2.5, label=r'$s=+1:\ (1-0.3u)/2$')
ax.plot(u, (1-a*u)/2, color=red, lw=2, ls='--', label=r'$s=-1:\ (1+0.3u)/2$')
ax.fill_between(u, 0, pdf, where=u<=0, color=blue, alpha=.17)
ax.fill_between(u, 0, pdf, where=u>=0, color=red, alpha=.17)
ax.axvline(0, color='#777777', lw=1)
ax.text(-.5, .20, 'Backward\nprobability 0.575', ha='center', fontsize=12)
ax.text(.5, .20, 'Forward\nprobability 0.425', ha='center', fontsize=12)
ax.set(xlim=(-1,1), ylim=(0,.84), xlabel=r'$u=\cos\theta$ (fixed laboratory axis)',
       ylabel=r'Probability density $d\Pr/du$')
ax.set_title('Angular law: unit total probability', fontsize=14, weight='bold', pad=13)
ax.legend(loc='upper center', frameon=False, fontsize=11)
ax.spines[['top','right']].set_visible(False)
ax.text(.5, -.17, r'Hemispheres: $k=1/2$, so $\epsilon=ak=-0.15$',
        transform=ax.transAxes, ha='center', fontsize=12)

counts = np.array([[6800,5750], [7360,3400]])
bar = fig.add_subplot(gs[0,1])
x=np.arange(2); w=.34
for i,(label,color) in enumerate(((r'$s=+1$',blue),(r'$s=-1$',red))):
    b=bar.bar(x+(i-.5)*w,counts[i],width=w,color=color,label=label)
    bar.bar_label(b,padding=4,fontsize=11)
bar.set_xticks(x,['Detector +','Detector −'])
bar.set(ylim=(0,10000),ylabel='Expected counts (chosen)')
bar.set_title('Stable unequal efficiencies, unequal exposures', fontsize=13, weight='bold', pad=14)
bar.legend(frameon=False, loc='upper right', ncols=2)
bar.spines[['top','right']].set_visible(False)
bar.set_yticks([0,4000,8000])
bot=fig.add_subplot(gs[1,1]); bot.axis('off')
bot.text(.5, .97, r'$\eta_+/\eta_-=0.8/0.5=1.6,\quad C_+/C_-=1.25$', ha='center', va='top', fontsize=12)
bot.text(.5, .55, r'$R=\frac{6800\times3400}{5750\times7360}=\frac{289}{529}$', ha='center', va='center', fontsize=17)
bot.text(.5, .05, r'$\sqrt{R}=17/23\quad\Rightarrow\quad\epsilon=-0.15$', ha='center', va='center', fontsize=15, color=blue)
fig.suptitle('Original teaching example: angular bias survives efficiency cancellation',
             fontsize=18, weight='bold', y=.975)
fig.text(.5,.88, r'Choose $A=-0.8$, $P=0.5$, $\beta=0.75$: $a=AP\beta=-0.3$ • matched opposite hemispheres',
         ha='center',fontsize=13)
fig.text(.5,.025,'All numbers are constructed • no background • equal-magnitude spin reversal • efficiencies stable between states',
         ha='center',fontsize=10,color='#555555')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
