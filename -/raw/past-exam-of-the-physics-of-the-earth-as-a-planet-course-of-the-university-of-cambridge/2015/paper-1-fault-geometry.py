from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig,ax=plt.subplots(1,3,figsize=(11.2,3.5),layout='constrained')
a=ax[0];a.set_title('Plan view: strike and dip side');a.plot([-1,1],[-.6,.6],color='#2469a0',lw=3)
a.annotate('',(.75,.45),(-.6,-.36),arrowprops=dict(arrowstyle='->',lw=2,color='#2469a0'))
a.annotate('',(0,1),(0,0),arrowprops=dict(arrowstyle='->',color='black'));a.text(0,1.05,'N',ha='center')
a.add_patch(Arc((0,0),1.1,1.1,theta1=31,theta2=90,color='#9e4a10'));a.text(.28,.55,'strike',fontsize=10)
a.annotate('dip side',(.6,-.9),(.15,-.3),ha='center',arrowprops=dict(arrowstyle='->',color='#9e4a10'))
a.set(xlim=(-1.2,1.2),ylim=(-1.15,1.15));a.set_aspect('equal');a.axis('off')
a=ax[1];a.set_title('Section perpendicular to strike');a.plot([-.2,2.5],[0,0],color='black');a.plot([0,2.1],[0,-1.4],lw=3,color='#2469a0')
a.plot(1.35,-.9,'*',ms=14,color='#c62828');a.plot(1.35,0,'o',color='#c62828');a.plot([1.35,1.35],[-.9,0],'--',color='gray')
a.text(1.42,-.95,'hypocentre',fontsize=10);a.text(1.4,.12,'epicentre',fontsize=10)
a.add_patch(Arc((0,0),1,1,theta1=-33.69,theta2=0,color='#9e4a10'));a.text(.6,-.18,r'$\delta$',color='#9e4a10',fontsize=13)
a.text(.9,-1.35,'fault plane',color='#2469a0');a.set(xlim=(-.2,2.8),ylim=(-1.6,.4));a.set_aspect('equal');a.axis('off')
a=ax[2];a.set_title('Fault plane unfolded: signed rake')
a.annotate('',(1.45,0),(-.1,0),arrowprops=dict(arrowstyle='->',color='#2469a0'));a.text(1.43,-.18,r'strike $\mathbf{s}$',ha='right',fontsize=10)
a.annotate('',(0,1.25),(0,-.25),arrowprops=dict(arrowstyle='->',color='#2469a0'));a.text(.08,1.35,r'up dip $-\mathbf{d}$',fontsize=10)
a.annotate('',(1,1),(0,0),arrowprops=dict(arrowstyle='->',lw=2,color='#c62828'));a.text(1.03,1.02,'slip',fontsize=10,color='#c62828')
a.add_patch(Arc((0,0),1,1,theta1=0,theta2=45,color='#9e4a10'));a.text(.57,.17,r'$\lambda$',fontsize=13)
a.text(.15,-.32,r'$+90^\circ$: up dip',fontsize=10);a.set(xlim=(-.2,1.85),ylim=(-.55,1.6));a.set_aspect('equal');a.axis('off')
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
