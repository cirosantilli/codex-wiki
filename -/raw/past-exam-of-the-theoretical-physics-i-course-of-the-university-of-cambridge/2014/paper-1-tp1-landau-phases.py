from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
c=np.linspace(-2,2,601);a=np.linspace(-1.5,1.5,501);C,A=np.meshgrid(c,a);phase=np.zeros_like(A);phase[(C>=0)&(A<0)]=1;phase[(C<0)&(A<C*C/4)]=2
fig,ax=plt.subplots(figsize=(6.2,4.2),layout='constrained');ax.pcolormesh(C,A,phase,cmap=ListedColormap(['#e7e7e7','#b5d4ee','#eac9a7']),shading='nearest',vmin=0,vmax=2)
x=np.linspace(-2,0,200);ax.plot(x,x*x/4,color='black');ax.plot([0,2],[0,0],color='black');ax.plot([0,0],[-1.5,0],color='black');ax.plot(0,0,'o',color='#c62828')
ax.text(.65,-.8,'uniform order',ha='center');ax.text(-1,-.8,'helical order',ha='center');ax.text(.65,.8,'disorder',ha='center');ax.annotate('Lifshitz point',(0,0),(.4,.3),arrowprops=dict(arrowstyle='->'),fontsize=10)
ax.text(-1.75,1.15,r'$a=c^2/4$',fontsize=11);ax.set(xlabel=r'$c$',ylabel=r'$a$',title='Mean-field minima for fourth-gradient coefficient 1')

fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
