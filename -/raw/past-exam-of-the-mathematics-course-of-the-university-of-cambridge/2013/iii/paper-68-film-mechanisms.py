"""Original physical diagrams. Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Preserves caller MPLCONFIGDIR; writes its PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(11,4.4),dpi=100,layout='constrained')
x=np.linspace(-3,3,500); h=1+.35*np.cos(np.pi*x/3)
for ax in axes:
    ax.fill_between(x,0,h,color='#d9eef9'); ax.plot(x,h,color='#235e83',lw=2); ax.axhline(0,color='#884f31',lw=4)
    ax.set(xlim=(-3,3),ylim=(-.35,2),xticks=[],yticks=[]); ax.spines[['top','right','left','bottom']].set_visible(False)
axes[0].set_title('Capillary pressure: stabilizing')
axes[0].text(0,1.58,'high pressure at crest',ha='center')
axes[0].text(-2.5,.63,'lower\npressure',ha='center'); axes[0].text(2.5,.63,'lower\npressure',ha='center')
for side in [-1,1]: axes[0].annotate('',xy=(2.3*side,.8),xytext=(.35*side,.8),arrowprops=dict(arrowstyle='->',lw=2,color='#235e83'))
axes[0].text(0,-.28,'Liquid flows away from the crest',ha='center')
axes[1].set_title('Cooling-induced Marangoni stress: destabilizing')
axes[1].text(0,1.63,'colder surface, higher tension',ha='center')
for side in [-1,1]: axes[1].annotate('',xy=(.4*side,1.43),xytext=(2.35*side,1.43),arrowprops=dict(arrowstyle='->',lw=2,color='#b33445'))
axes[1].text(-2.3,.52,'warmer\nsurface',ha='center'); axes[1].text(2.3,.52,'warmer\nsurface',ha='center')
axes[1].text(0,-.28,'Surface flow feeds the crest',ha='center')
fig.savefig('paper-68-film-mechanisms.png',facecolor='white',transparent=False)
