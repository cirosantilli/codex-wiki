"""Synthetic magnesium spectra; neutral masses approximate ion masses.

Modern input data, not historical Aston observations:
https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ascii=ascii&ele=Mg
Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired output directory; emits this script's basename.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

masses = np.array([23.985041697, 24.985836976, 25.982592968])
fractions = np.array([.7899, .1000, .1101])
colors = ['#16749b', '#b94b20', '#7754a3']
plt.rcParams.update({'font.size': 10, 'figure.facecolor':'white', 'axes.facecolor':'white'})
fig = plt.figure(figsize=(10.8, 8))
gs = fig.add_gridspec(3, 2, height_ratios=[1.05, 1, .83], hspace=.72, wspace=.25)
a=fig.add_subplot(gs[0,:])
for z,scale in ((1,1), (2,.28)):
    for i,(m,f,c) in enumerate(zip(masses,fractions,colors)):
        x=m/z
        a.vlines(x,0,scale*f,color=c,lw=3)
        a.annotate(f'{24+i}, z={z}', xy=(x,scale*f), xytext=(x + ((-.24, 0, .24)[i] if z==2 else 0), scale*f + ((.10,.23,.10)[i] if z==2 else .025)), ha='center', fontsize=9, arrowprops={'arrowstyle':'-', 'color':c, 'lw':.7} if z==2 else None)
a.set(xlim=(10.5,27.6),ylim=(0,.96),xlabel='x = (m / u) / z     [dimensionless]',ylabel='Chosen line area')
a.set_title('A. The same three isotopes occupy two charge-state groups', loc='left',weight='bold')
a.text(15.9,.58,'Doubly charged yield chosen as 0.28 × singly charged yield.\nPositions approximate ion masses by neutral masses.',fontsize=9)
xs=np.linspace(22.3,27.7,5000)
for j,width in enumerate((.12,1.20)):
    ax=fig.add_subplot(gs[1,j])
    sigma=width/(2*np.sqrt(2*np.log(2)))
    components=[f*np.exp(-.5*((xs-m)/sigma)**2)/(sigma*np.sqrt(2*np.pi)) for m,f in zip(masses,fractions)]
    for y,c in zip(components,colors):ax.plot(xs,y,color=c,lw=1.4)
    ax.plot(xs,np.sum(components,axis=0),color='#292929',lw=1.3,ls='--',label='Sum')
    ax.set(xlim=(22.6,27.4),xlabel='x',ylabel='Signal per unit x')
    ax.set_title(f'{"B" if j==0 else "C"}. Chosen FWHM = {width:.2f}; R₂₅ ≈ {masses[1]/width:.1f}',loc='left',weight='bold',fontsize=11)
    ax.legend(frameon=False,fontsize=9)
ax=fig.add_subplot(gs[2,:])
p=np.arange(3)
biased=fractions*np.array([1,2,1]);biased/=biased.sum()
ax.bar(p-.18,fractions,width=.34,label='Neutral isotope fractions',color='#16749b')
ax.bar(p+.18,biased,width=.34,label='Normalized areas: mass-25 response × 2',color='#c87933')
for i,(f,b) in enumerate(zip(fractions,biased)):
    ax.text(i-.18,f+.015,f'{f:.4f}',ha='center',fontsize=9)
    ax.text(i+.18,b+.015,f'{b:.4f}',ha='center',fontsize=9)
ax.set(xticks=p,xticklabels=['Mass number 24','Mass number 25','Mass number 26'],ylim=(0,1.04),ylabel='Fraction')
ax.set_title('D. A response change alters inferred fractions without altering the sample',loc='left',weight='bold')
ax.legend(frameon=False,loc='upper right',fontsize=9)
for ax in fig.axes:
    ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.075,right=.98,top=.94,bottom=.09)
fig.text(.075,.025,'Original synthetic illustration: no measured counts, historical masses, or historical resolution are inferred.',fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),dpi=120,facecolor='white')
plt.close(fig)
