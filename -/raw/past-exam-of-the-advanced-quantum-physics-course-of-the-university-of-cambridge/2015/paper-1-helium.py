"""Original explanatory plot. Python 3.14, numpy, matplotlib.
Run from the destination directory; writes a PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
# Original energy-level drawing; numerical wavenumbers from the NIST He I table.
cm_to_eV=6.62607015e-34*299792458*100/1.602176634e-19
fig,(ax,bottom)=plt.subplots(2,1,figsize=(8,6),sharex=True,gridspec_kw={'height_ratios':[4,1]},layout='constrained')
levels=[(.2,1.05,166277.4403,r'$1s2s\;{}^1S_0$'),(.2,1.05,171134.8970,r'$1s2p\;{}^1P_1^{o}$'),(1.7,2.55,159855.9745,r'$1s2s\;{}^3S_1$'),(1.7,2.55,169086.7666,r'$1s2p\;{}^3P_{0,1,2}^{o}$')]
for lo,hi,w,t in levels:
 e=w*cm_to_eV;ax.plot([lo,hi],[e,e],color='#1766a5' if lo<1 else '#c33c29',lw=2);ax.text((lo+hi)/2,e+.13,t,ha='center',fontsize=11)
limit=198310.6691*cm_to_eV;ax.axhline(limit,ls='--',color='gray');ax.text(1.4,limit+.12,'He II ground-state limit',ha='center');bottom.plot([.2,1.05],[0,0],color='#1766a5',lw=2);bottom.text(.625,.17,r'$1s^2\;{}^1S_0$',ha='center',fontsize=11)
ax.set(ylim=(19.3,25.4),ylabel='Excitation energy (eV)',title='Neutral helium: singlet and triplet families');bottom.set(ylim=(-.35,.8),xlim=(-.1,2.85),xticks=[.625,2.125],xticklabels=['Singlet, S = 0','Triplet, S = 1']);bottom.spines.top.set_visible(False);ax.spines.bottom.set_visible(False);ax.tick_params(labelbottom=False,bottom=False)
for a,y in [(ax,0),(bottom,1)]:
 for xp in [0,1]:a.plot([xp-.012,xp+.012],[y-.02,y+.02],transform=a.transAxes,color='black',clip_on=False,lw=1)
fig.suptitle('Broken energy axis; triplet P fine structure is unresolved.',fontsize=9)
fig.savefig('paper-1-helium.png',dpi=170);plt.close(fig)
