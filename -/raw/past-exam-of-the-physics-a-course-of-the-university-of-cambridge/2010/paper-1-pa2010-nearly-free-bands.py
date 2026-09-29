"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
V=.02;ns=np.arange(-3,4);q=np.linspace(-.5,.5,801)
def bands(x):
 H=np.diag((x+ns)**2);H+=np.diag(np.full(6,V),1)+np.diag(np.full(6,V),-1);return np.linalg.eigvalsh(H)
values=np.array([bands(x) for x in q]);free=np.sort((q[:,None]+ns[None,:])**2,axis=1)
fig,axs=plt.subplots(1,2,figsize=(10.2,4.8),layout='constrained')
extended=np.linspace(-1,1,1401)
axs[0].plot(extended,extended**2,'--',color='gray',label='Unperturbed parabola')
axs[0].plot(q,values[:,0],color='#2a6b9a',label='Weak periodic potential')
for sign in [-1,1]:
 outer=np.linspace(.5,1,401)*sign;energy=np.array([bands(x-sign)[1] for x in outer]);axs[0].plot(outer,energy,color='#2a6b9a')
axs[0].axvspan(-.5,.5,color='#b9d6ed',alpha=.22);axs[0].annotate('',xy=(.5,1.0),xytext=(-.5,1.0),arrowprops={'arrowstyle':'<->'});axs[0].text(0,1.02,'One reciprocal vector G',ha='center',fontsize=9)
axs[0].set(title='Extended-zone view',xlabel='Wavevector / G',ylabel='Energy / free energy at G',ylim=(-.02,1.27));axs[0].legend(fontsize=9,loc='upper left')
for n in range(3):
 axs[1].plot(q,free[:,n],':',color='gray');axs[1].plot(q,values[:,n],color=['#28699a','#a14a28','#2d805e'][n])
qF=(6*np.pi**2)**(1/3)/(2*np.sqrt(2)*np.pi);eb=bands(qF)
axs[1].annotate('',xy=(qF,eb[1]),xytext=(qF,eb[0]),arrowprops={'arrowstyle':'->','color':'black','lw':1.8});axs[1].text(.08,.47,'Optical step',fontsize=9)
axs[1].set(title='Folded bands in the first zone',xlabel='Reduced wavevector / G',ylabel='Energy / free energy at G',ylim=(-.02,1.15),xlim=(-.5,.5))
for ax in axs:
 for edge in [-.5,.5]:ax.axvline(edge,color='gray',ls=':',lw=.8)
 ax.grid(alpha=.15)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
