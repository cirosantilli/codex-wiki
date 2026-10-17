"""Original 13C assignment maps for NST IA Chemistry 2024; Python 3.14."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axs=plt.subplots(4,1,figsize=(10.2,7.8),facecolor='white')
def text(ax,x,y,s,fs=13,c='black'):
    ax.text(x,y,s,ha='center',va='center',fontsize=fs,color=c,bbox={'facecolor':'white','edgecolor':'none','pad':1})
for ax in axs:
    ax.set(xlim=(-.5,11.7),ylim=(-1.2,1.65));ax.axis('off')
# Six-membered diketone: original geometry and labels, not a supplied figure.
a=axs[0];pts=np.array([[0,1],[.87,.5],[.87,-.5],[0,-1],[-.87,-.5],[-.87,.5]])+[3.0,.1]
for u,v in zip(pts,np.roll(pts,-1,axis=0)):a.plot([u[0],v[0]],[u[1],v[1]],color='black',lw=1.4)
for i in [0,3]:
    u=pts[i];v=u+np.array([0,.5 if i==0 else -.5]);a.plot([u[0]-.05,v[0]-.05],[u[1],v[1]],color='black');a.plot([u[0]+.05,v[0]+.05],[u[1],v[1]],color='black');text(a,*v,r'$\mathrm{O}$',12)
a.text(.0,1.1,'A / spectrum 5',weight='bold',fontsize=12)
text(a,7.8,.6,'Both carbonyl C: 208.3 ppm',13,'#245f8a');text(a,7.8,-.3,'All four CH₂: 36.5 ppm',13,'#245f8a')
def chain(ax,label,atoms,shifts,bonds):
    ax.text(0,1.36,label,weight='bold',fontsize=12)
    xs=np.linspace(.4,10.6,len(atoms))
    for i,(atom,shift) in enumerate(zip(atoms,shifts)):
        text(ax,xs[i],.25,atom,14);text(ax,xs[i],-.5,shift,12,'#245f8a')
    for i,b in enumerate(bonds):
        for off in ([0] if b==1 else [-.055,.055] if b==2 else [-.09,0,.09]):
            ax.plot([xs[i]+.57,xs[i+1]-.57],[.25+off,.25+off],color='black',lw=1.2)
chain(axs[1],'B / spectrum 8',[r'$\mathrm{HOOC}$',r'$\mathrm{CH}$',r'$\mathrm{CH}$',r'$\mathrm{CH}$',r'$\mathrm{CH}$',r'$\mathrm{CH_3}$'],['172.8','118.1','147.4','129.7','140.8','18.1'],[1,2,1,2,1])
chain(axs[2],'C / spectrum 6',[r'$\mathrm{HOOC}$',r'$\mathrm{C}$',r'$\mathrm{C}$',r'$\mathrm{CH_2}$',r'$\mathrm{CH_2}$',r'$\mathrm{CH_3}$'],['158.5','72.9','92.6','20.7*','21.0*','13.4'],[1,3,1,1,1])
axs[2].text(5.5,-1.02,'* The two methylene assignments may be interchanged from the shift list alone.',ha='center',fontsize=10)
chain(axs[3],'D / spectrum 7',[r'$\mathrm{CH_3}$',r'$\mathrm{CH}$',r'$\mathrm{CH}$',r'$\mathrm{C(=O)}$',r'$\mathrm{O}$',r'$\mathrm{CH}$',r'$\mathrm{CH_2}$'],['18.2','148.0','121.7','163.2','','141.3','97.4'],[1,2,1,1,1,2])
fig.text(.5,.015,'Blue numbers are ¹³C chemical shifts in ppm. Connectivity is shown in condensed form.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,1),h_pad=.3)
fig.savefig('paper-1-carbon-assignments.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
