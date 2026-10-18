"""Original conditional capture and reversal models, not measurements.
Python 3.14, NumPy 2.3, Matplotlib 3.10. Outputs only basename PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10.5,4.5),facecolor='white');f=np.linspace(0,1,801)
a=6-5*f;bb=2+5*f;va=np.log(6/a);vb=-a/bb*va;ok=(va-1<vb)
for data,label,color in [(va,'A','#b14c29'),(vb,'B','#236b8e')]:
 axs[0].plot(f,np.where(ok,data,np.nan),color=color,label=label,lw=2)
 axs[0].plot(f,np.where(~ok,data,np.nan),color=color,ls='--',lw=2)
axs[0].axvline(.4,color='gray',ls=':',lw=1);s=np.log(1.5);axs[0].scatter([.4,.4],[s,-s],c='black',s=18,zorder=5)
axs[0].annotate('Equal speeds at f = 0.40',(.4,s),xytext=(.06,1.35),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[0].text(.49,.16,'Dashed: imposed collection\nwithout ballistic interception',fontsize=8.5)
axs[0].set(title=r'$m_B=2m_A,\ M=5m_A$',ylabel=r'Signed velocity / $u_0$');axs[0].legend(loc='upper left')
vr=np.log(2/1.55);vbr=-1.55/2.45*vr
va=np.where(f<=.45,np.log(2/(2-f)),vr+np.log((2-f)/1.55));vb=np.where(f<=.45,-(2-f)/(2+f)*np.log(2/(2-f)),vbr)
axs[1].plot(f,va,color='#b14c29',label='A',lw=2);axs[1].plot(f,vb,color='#236b8e',label='B',lw=2);axs[1].axvline(.45,color='gray',ls=':',lw=1)
axs[1].annotate('Reverse exhaust',(.45,vr),xytext=(.51,.18),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].text(.10,-.21,'Final closing speed = 0.02210 u₀',fontsize=9)
axs[1].set(title=r'$M=m_A=m_B/2$',ylabel=r'Signed velocity / $u_0$',ylim=(-.25,.32));axs[1].legend(loc='upper left')
for a in axs:a.set_xlabel('Fraction f of original fuel consumed');a.axhline(0,color='gray',lw=.7);a.grid(alpha=.18);a.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path('2014-exhaust-collection-speeds.png'),dpi=140,facecolor='white')
