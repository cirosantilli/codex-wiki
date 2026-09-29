"""Original selective-contact diagram and chosen diode curves, Python 3.14.

No measured device data. Write PNG basename to the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(11,5.0),layout='constrained',gridspec_kw={'width_ratios':[1.25,1]})
fig.patch.set_facecolor('white')
ax=axes[0]
ax.set(xlim=(-.2,7.4),ylim=(-.5,2.4))
ax.axis('off')
ax.add_patch(Rectangle((1.5,-.1),4.5,1.8,fc='#f5f0e8',ec='none'))
ax.add_patch(Rectangle((.05,-.1),1.25,.2,fc='#dbe8f4',ec='#547996'))
ax.add_patch(Rectangle((6.2,1.5),1.0,.2,fc='#dceee5',ec='#5c8c74'))
for y,lab in [(0,r'$E_v$'),(1.6,r'$E_c$')]:
    ax.plot([1.5,6],[y,y],color='#4e5e70',lw=1.8)
    ax.text(1.35,y,lab,ha='right',va='center',fontsize=12)
ax.plot([.05,6],[.3,.3],ls='--',color='#a95136')
ax.plot([1.5,7.2],[1.3,1.3],ls='--',color='#2e7395')
ax.text(6.3,1.17,r'$E_{Fn}$',fontsize=12,color='#2e7395')
ax.text(.15,.4,r'$E_{Fp}$',fontsize=12,color='#a95136')
ax.text(.65,-.35,'Hole-selective\ncontact',ha='center',fontsize=10)
ax.text(6.7,-.35,'Electron-selective\ncontact',ha='center',fontsize=10)
ax.text(3.7,2.15,'Perovskite absorber',ha='center',fontsize=12)
ax.annotate('',xy=(2.1,1.6),xytext=(2.1,0),arrowprops={'arrowstyle':'->','color':'#c18b2e','lw':2})
ax.text(1.85,1.9,'Light',ha='center',fontsize=10,color='#9c7025')
ax.annotate('',xy=(3.1,0),xytext=(3.1,1.6),arrowprops={'arrowstyle':'->','color':'#367b65','lw':1.7})
ax.text(2.91,.8,'Radiative',rotation=90,ha='right',va='center',fontsize=10,color='#367b65')
ax.plot([4.15,4.8],[.8,.8],color='#975383',lw=1.6)
for top,bottom in [(1.6,.84),(.76,0)]:
    ax.annotate('',xy=(4.45,bottom),xytext=(4.45,top),arrowprops={'arrowstyle':'->','color':'#975383','lw':1.7})
ax.text(4.86,.8,'Trap / SRH',fontsize=10,va='center',color='#975383')
ax.annotate('',xy=(5.8,1.3),xytext=(5.8,.3),arrowprops={'arrowstyle':'<->','color':'#4d5863','lw':1.4})
ax.text(5.94,.48,r'$qV_{OC}$',rotation=90,va='bottom',fontsize=11)
ax.text(3.7,-.35,'Interface losses can further reduce terminal splitting',ha='center',fontsize=9.5)
ax.set_title('Qualitative illuminated energy levels',fontsize=12)
ax=axes[1]
vt=.02585
voltage=np.linspace(0,1.34,700)
for voc,label,color in [(1.30,'Lower recombination','#327e75'),(1.02,'Higher recombination','#a5533f')]:
    j0=1/np.expm1(voc/vt)
    current=1-j0*np.expm1(voltage/vt)
    ax.plot(voltage,current,label=label,color=color,lw=2)
    ax.scatter([voc],[0],c=color,s=30,zorder=3)
ax.axhline(0,color='0.55',lw=.8)
ax.set(xlim=(0,1.35),ylim=(-.12,1.1),xlabel='Voltage (chosen V)',ylabel=r'$J/J_{SC}$',title='Stipulated diode curves; equal photocurrent')
ax.legend(loc='lower left',fontsize=10)
ax.grid(alpha=.18)
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-additional-solar-cell.png',dpi=160,facecolor='white')
plt.close(fig)
