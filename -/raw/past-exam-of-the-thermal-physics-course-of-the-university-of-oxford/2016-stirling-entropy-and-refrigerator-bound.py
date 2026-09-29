from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.5),dpi=125,facecolor='white')
c=1.5;lnr=1;Th=2;Tc=1
T=np.linspace(Tc,Th,300);S=c*np.log(T/Th)
ax.plot([0,lnr],[Th,Th],color='#b13939',lw=2.3)
ax.plot(S+lnr,T,color='#2268a3',lw=2.3)
ax.plot([S[0]+lnr,S[0]],[Tc,Tc],color='#26764e',lw=2.3)
ax.plot(S,T,color='#2268a3',lw=2.3)
points=[(0,Th),(lnr,Th),(S[0]+lnr,Tc),(S[0],Tc)]
for i,(sv,tv) in enumerate(points,1):
 ax.plot(sv,tv,'ko',ms=4);ax.annotate(str(i),(sv,tv),xytext=(5,8 if tv>1 else -16),textcoords='offset points',fontsize=12)
ax.annotate('',xy=(.75,2),xytext=(.3,2),arrowprops={'arrowstyle':'->','lw':1.5})
ax.annotate('',xy=(S[0]+.25,1),xytext=(S[0]+.7,1),arrowprops={'arrowstyle':'->','lw':1.5})
idx=160
ax.annotate('',xy=(S[idx+30]+1,T[idx+30]),xytext=(S[idx]+1,T[idx]),arrowprops={'arrowstyle':'<-','lw':1.5})
ax.annotate('',xy=(S[idx+30],T[idx+30]),xytext=(S[idx],T[idx]),arrowprops={'arrowstyle':'->','lw':1.5})
ax.fill_betweenx(T,S,S+1,color='#dce8f1',alpha=.65)
ax.text(-.13,1.47,r'Area $=W/(nRT_c)$',ha='center',fontsize=10)
ax.set(xlim=(-1.3,1.3),ylim=(.84,2.2),xlabel=r'$(S-S_1)/(nR)$',ylabel=r'$T/T_c$',title=r'Gas cycle: $T_h/T_c=2$, $\ln r=1$')
logr=np.linspace(.1,4,500);bound=277.15/16
bx.plot(logr,bound-1.5/logr,lw=2.4,color='#2268a3',label='Unregenerated neon model')
bx.axhline(bound,color='#26764e',ls='--',lw=1.5,label=f'Carnot bound {bound:.3f}')
bx.axhline(19,color='#b13939',ls=':',lw=2,label='Stated performance 19')
bx.set(xlim=(0,4),ylim=(0,20.2),xlabel=r'$\ln(V_2/V_1)>0$',ylabel=r'Cooling COP $Q_c/W$',title='Given temperatures: 277.15 K and 293.15 K')
bx.legend(loc='lower right',fontsize=9,frameon=True,facecolor='white')
for a in (ax,bx):
 a.spines[['top','right']].set_visible(False);a.grid(alpha=.15);a.set_facecolor('white')
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
