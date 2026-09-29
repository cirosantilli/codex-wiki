"""Original population-region sketch; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run in the intended output directory. Output is a same-basename opaque white PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,2,figsize=(10,4.5),dpi=120,facecolor='white')
rg='#edbd58'; wd='#80b4df'; ms='#edf1f4'
m=np.linspace(0.1,3.5,1800)
lo=9/m; hi=np.minimum(10/m,10)
a=axes[0]
a.set_facecolor(ms)
a.fill_between(m,lo,hi,where=lo<hi,color=rg)
a.fill_between(m,10/m,10,where=m>=1,color=wd)
a.plot(m,9/m,color='#915800',label=r'$t/\mathrm{Gyr}=9/m$')
a.plot(m,10/m,color='#155489',label=r'$t/\mathrm{Gyr}=10/m$')
a.set(xlim=(0.1,3.5),ylim=(0,10),xlabel=r'Initial mass $m=M/M_\odot$',ylabel=r'Present age $t/\mathrm{Gyr}$',title='Mass and age')
a.text(2.2,5.6,'White dwarf',ha='center'); a.text(2.5,1.6,'Main sequence',ha='center')
a.annotate('Red giant',xy=(2,4.75),xytext=(1.9,7.5),arrowprops={'arrowstyle':'->'},ha='center')
a.set_xticks([.1,1,2,3]); a.legend(loc='upper right',fontsize=9)
y=np.linspace(0,1,600); a=axes[1]; a.set_facecolor(ms)
a.fill_betweenx(y,0,y/10,color=wd)
a.fill_betweenx(y,y/10,y/9,color=rg)
a.plot(y/10,y,color='#155489',label=r'$Y=10X$')
a.plot(y/9,y,color='#915800',label=r'$Y=9X$')
a.set(xlim=(0,.14),ylim=(0,1),xlabel=r'$X=0.1/m$',ylabel=r'$Y=t/(10\,\mathrm{Gyr})$',title='Evolved region in uniform coordinates')
a.text(.034,.8,'White dwarf',ha='center'); a.text(.122,.45,'Main\nsequence',ha='center')
a.annotate('Red giant',xy=(.069,.65),xytext=(.047,.24),arrowprops={'arrowstyle':'->'},ha='center')
a.set_xticks([0,.05,.1,1/9,.14],labels=['0','.05','.1','1/9','.14']);a.legend(loc='upper left',fontsize=9)
fig.text(.5,.018,'Right: enlarged view of X ≤ 0.14. The rest of the unit square, 0.14 < X ≤ 1, is main sequence.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.055,1,1));fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
