"""Original analytic free-electron DOS and occupation, strictly at T=0.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
Outputs fermi-sea-density-of-states-occupation.png to the current directory.
Both spin states are included. Curves are model functions, not measured data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.5,4.6),dpi=110)
x=np.linspace(0,2.0,801)
ax.plot([0,1,1,2],[1,1,0,0],lw=2.5,color='#145b87')
ax.fill_between([0,1],[1,1],color='#c6e2f2',alpha=.75)
ax.axvline(1,color='#bc5722',ls=':',lw=1.6)
ax.text(.12,.49,'Every complete state\nbelow the edge is filled',color='#145b87',fontsize=10)
ax.text(1.19,.49,'Empty\nstates',color='#6a7279')
ax.set(xlabel=r'Energy $x=E/E_F$',ylabel=r'Mean occupation $f(E)$',
       xlim=(0,2),ylim=(-.06,1.15),title='Occupation per state')
ax.set_yticks([0,1])

y=1.5*np.sqrt(x)
occupied=x<=1
bx.plot(x,y,color='#8a9299',ls='--',lw=2,label='Available states')
bx.fill_between(x[occupied],y[occupied],color='#c6e2f2')
bx.plot(x[occupied],y[occupied],color='#145b87',lw=2.5,label='Occupied states')
bx.plot([1,1,2],[1.5,0,0],color='#145b87',lw=2.5)
bx.axvline(1,color='#bc5722',ls=':',lw=1.6)
bx.text(.22,.35,'Shaded area = 1',fontsize=11,color='#145b87')
bx.text(1.23,.65,'Available,\nbut empty',color='#6a7279')
bx.set(xlabel=r'Energy $x=E/E_F$',ylabel=r'States per $dx$, divided by $N$',
       xlim=(0,2),ylim=(-.06,2.4),title=r'Count per energy: $(E_F/N)g(E)=\frac{3}{2}\sqrt{x}$')
bx.legend(frameon=False,loc='upper left',fontsize=10)
for a in (ax,bx):
    a.set_xticks([0,.5,1,1.5,2]);a.spines[['top','right']].set_visible(False)
    a.grid(axis='y',alpha=.12)
fig.suptitle('The zero-temperature Fermi sea has an energy edge',fontsize=15,y=.98)
fig.text(.5,.025,r'Two spin states; uniform 3D nonrelativistic model.  '+
         r'$\langle E\rangle/E_F=\int_0^1 x\,\frac{3}{2}\sqrt{x}\,dx=\frac{3}{5}$.',ha='center',fontsize=11)
fig.subplots_adjust(left=.075,right=.98,bottom=.2,top=.78,wspace=.32)
fig.savefig(Path.cwd()/'fermi-sea-density-of-states-occupation.png',facecolor='white')
plt.close(fig)
