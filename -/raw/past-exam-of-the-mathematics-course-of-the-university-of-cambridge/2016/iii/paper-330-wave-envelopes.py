"""Original internal-wave schematics. Python 3.14; numpy 2.3.5, matplotlib 3.10.7.
Run in the output cwd; Make creates the final mirrored _media PNG.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
 fig,axes=plt.subplots(1,3,figsize=(13.8,4.6000001),dpi=100,facecolor='white')
 theta=np.linspace(.003,np.pi/2-.003,6000);co=np.cos(theta);si=np.sin(theta);tau=1/(si*co);cos2=.5*co;sin2=np.sqrt(1-cos2*cos2)
 for ax,t,label in zip(axes[:2],[2.,4.],['First arrival: t = T','Refracted fronts: t = 2T']):
  x=t*co*co;z=t*si*co;ground=np.linspace(0,t,400);envelope=np.sqrt(np.maximum(0,(t/2)**2-(ground-t/2)**2));ax.fill_between(ground,0,np.minimum(envelope,1),color='#e9f2f7',zorder=0)
  direct=z<=1+1e-7;ax.plot(np.where(direct,x,np.nan),np.where(direct,z,np.nan),color='#226ca1',lw=2,label='Direct front')
  crossed=tau<=t+1e-7;xt=co/si+(t-tau)*.5*cos2*cos2;zt=1+(t-tau)*.5*sin2*cos2
  if crossed.any():ax.plot(xt[crossed],zt[crossed],color='#26856a',lw=2,label='Transmitted front')
  zr=2-z;returned=crossed&(zr>=-1e-7);ax.plot(x[returned],zr[returned],color='#b36a29',lw=1.8,ls='--',label='Reflected front')
  if t==2:ax.scatter([1],[1],s=28,color='#26856a',zorder=4);ax.annotate('(H, H)',(1,1),xytext=(1.2,1.22),fontsize=9,arrowprops={'arrowstyle':'-','color':'#777777'})
  ax.set_title(label,fontsize=11);ax.legend(fontsize=8,loc='upper right');ax.set_xlim(0,4.2);ax.set_ylim(0,1.65)
 ax=axes[2];levels=[.6,1.,1.4,1.9,2.5,3.2,4.]
 for level in levels:
  p=np.linspace(0,np.pi/2,500);x=level*np.cos(p);z=level*np.sin(p);mask=z<=1;ax.plot(x[mask],z[mask],color='#226ca1',lw=1,ls=':')
  boundary_phase=1/si;k=co;elapsed=(level-boundary_phase)/(.5*k);mask=elapsed>=0
  x=co/si+elapsed*.5*cos2*cos2;z=1+elapsed*.5*sin2*cos2;ax.plot(x[mask],z[mask],color='#26856a',lw=1,ls=':')
  if level>=1:
   p=np.linspace(0,np.pi/2,500);x=level*np.cos(p);z=2-level*np.sin(p);mask=(z>=0)&(z<=1);ax.plot(x[mask],z[mask],color='#b36a29',lw=.8,ls=':')
 ax.set_title('Permanent phase curves',fontsize=11);ax.set_xlim(0,4.2);ax.set_ylim(0,1.65);ax.text(.16,1.46,r'$U_2=U_1/2$',fontsize=10);ax.text(2.25,.22,'Direct',color='#226ca1',fontsize=9);ax.text(2.15,1.3,'Transmitted',color='#26856a',fontsize=9)
 for ax in axes:
  ax.axhline(1,color='#999999',lw=1);ax.text(3.67,1.025,'z = H',fontsize=8,color='#666666');ax.scatter([0],[0],s=32,color='black',zorder=5);ax.set_xlabel('x / H');ax.set_ylabel('z / H');ax.grid(alpha=.15)
 fig.subplots_adjust(left=.045,right=.985,bottom=.14,top=.9,wspace=.27)
 fig.savefig('paper-330-wave-envelopes.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
