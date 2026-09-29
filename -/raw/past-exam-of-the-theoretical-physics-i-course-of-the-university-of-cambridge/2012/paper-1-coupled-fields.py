"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(2,1,figsize=(9,5.7),layout='constrained',sharex=True);m=1.;q=.7;g=.4;t=np.linspace(0,40,6000);wp=np.sqrt(q*q+m*m-g);wm=np.sqrt(q*q+m*m+g);bar=(wm+wp)/2;delta=(wm-wp)/2
f1=(np.cos(wp*t)+np.cos(wm*t))/2;f2=(np.cos(wp*t)-np.cos(wm*t))/2;v1=(-wp*np.sin(wp*t)-wm*np.sin(wm*t))/2;v2=(-wp*np.sin(wp*t)+wm*np.sin(wm*t))/2
axs[0].plot(t,f1,color='#326b98',lw=1,label='field 1 amplitude / A');axs[0].plot(t,f2,color='#b76842',lw=1,label='field 2 amplitude / A');axs[0].plot(t,np.cos(delta*t),'--',color='#326b98',alpha=.4);axs[0].plot(t,np.sin(delta*t),'--',color='#b76842',alpha=.4);axs[0].set(ylabel='mode amplitude',title='Different normal frequencies produce original-field amplitude beating');axs[0].legend(fontsize=8,ncol=2);axs[0].grid(alpha=.15)
e1=(v1*v1+(q*q+m*m)*f1*f1)/2;e2=(v2*v2+(q*q+m*m)*f2*f2)/2;ei=-g*f1*f2;e0=(q*q+m*m)/2
for e,col,lab in [(e1,'#326b98','uncoupled field 1'),(e2,'#b76842','uncoupled field 2'),(ei,'#777777','interaction'),(e1+e2+ei,'#2b7a4b','total')]:axs[1].plot(t,e/e0,color=col,label=lab,lw=1)
axs[1].set(xlabel=r'time $mt$',ylabel='modal energy / initial total',ylim=(-.25,1.2));axs[1].legend(fontsize=8,ncol=4,loc='upper right');axs[1].grid(alpha=.15)
fig.suptitle(r'Illustration in natural units: $m=1$, $|q|=0.7$, $g=0.4$; no supplied numerical data')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
