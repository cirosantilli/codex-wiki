from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,3,figsize=(9.8,3.4),layout='constrained')
for a,K2,title in zip(ax,[2,1,.4],[r'$K^2>b^2$',r'$K^2=b^2$',r'$0<K^2<b^2$']):
 b=1.;root=np.sqrt(complex(K2-b*b));poles=[1j*b+root,1j*b-root]
 a.axhline(0,color='gray');a.axvline(0,color='gray');a.plot([v.real for v in poles],[v.imag for v in poles],'x',ms=9,mew=2,color='#9e4a10')
 if K2==1:a.text(.1,1.12,'double pole',fontsize=10)
 a.set(xlim=(-1.5,1.5),ylim=(-.2,2.2),xlabel=r'$\mathrm{Re}\,\omega$',ylabel=r'$\mathrm{Im}\,\omega$',title=title);a.grid(alpha=.15)
fig.suptitle(r'Illustration with $b=e\gamma=1$: all poles above the real axis',fontsize=11)

fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
