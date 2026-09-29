"""Original rarefaction and early-extinction diagrams. Python 3.14; numpy/matplotlib.
Only writes its PNG basename to the output cwd.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def panel(ax,a):
 b=a/2;zm=.8;L=.2;D=(1-b)*zm;A=a*L;threshold=1-np.sqrt(2/3);t1=L/a;t2=zm/(1-b);h1=1-(1-a)*t1;h2=b*t2;hf=.6*a;early=a<threshold
 tf=(1-hf)/(1-a) if early else (np.sqrt(A)+np.sqrt(D))**2;te=D/(1-a)**2;ze=zm+(2*a-1)*te
 t=np.linspace(0,tf,1200)
 top=1-(1-a)*t if early else np.where(t<=t1,1-(1-a)*t,zm-t+2*np.sqrt(A*t))
 bottom=np.where(t<=t2,b*t,zm+t-2*np.sqrt(D*t))
 if early:bottom=np.where(t>te,ze+a*(t-te),bottom)
 for phi in np.linspace(b,a,16):
  z=zm+(2*phi-1)*t;mask=(z>=bottom)&(z<=top);ax.plot(t[mask],z[mask],color='#bbbfc7',lw=.8)
 for phi in [b,a]:
  z=zm+(2*phi-1)*t;mask=(z>=bottom)&(z<=top);ax.plot(t[mask],z[mask],color='#777777',ls='--',lw=1)
 if not early:
  phi=np.sqrt(A)/(np.sqrt(A)+np.sqrt(D));ax.plot([0,tf],[zm,hf],color='#a16132',ls=':',lw=2,label='Last characteristic')
 ax.plot(t,top,color='#226ca1',lw=2,label='Clear-fluid front');ax.plot(t,bottom,color='#29856b',lw=2,label='Deposit front');ax.plot([tf,1.32],[hf,hf],color='#333333',lw=2)
 for tt,hh,label in [(t2,h2,r'$(t_{c2},h_{c2})$'),(tf,hf,r'$(t_c,h_c)$')]:
  ax.scatter([tt],[hh],color='black',s=23,zorder=5)
  offset=(-.31,.2) if tt==tf else (-.39,.08)
  ax.annotate(label,(tt,hh),xytext=(tt+offset[0],hh+offset[1]),fontsize=9,arrowprops={'arrowstyle':'-','color':'#888888'})
 if early:
  ax.scatter([te],[ze],color='#a16132',s=23,zorder=5);ax.annotate(r'Fan ends: $(t_e,z_e)$',(te,ze),xytext=(.48,.36),fontsize=9,arrowprops={'arrowstyle':'-','color':'#888888'})
 else:
  ax.scatter([t1],[h1],color='black',s=23,zorder=5);ax.annotate(r'$(t_{c1},h_{c1})$',(t1,h1),xytext=(.73,.74),fontsize=9,arrowprops={'arrowstyle':'-','color':'#888888'})
 ax.text(.03,.95,r'$\phi=a$',fontsize=10);ax.text(.035,.46,r'$\phi=a/2$',fontsize=10);ax.text(1.14,.83,r'$\phi=0$',fontsize=10);ax.text(.12,.025,r'$\phi=1$',fontsize=10);ax.text(.39,.63,'Rarefaction fan',fontsize=9,color='#666666');ax.axvline(tf,color='#bbbbbb',lw=1,ls=':');ax.axhline(hf,color='#bbbbbb',lw=1,ls=':');ax.set(xlim=(0,1.32),ylim=(0,1.02),xlabel=r'$u_st/H$',ylabel='z / H');ax.grid(alpha=.14)

def main():
 fig,axes=plt.subplots(1,2,figsize=(11.5,4.8),dpi=100,facecolor='white');panel(axes[0],.3);panel(axes[1],.1);axes[0].set_title(r'Both fronts enter the fan: $a=0.3$');axes[1].set_title(r'Fan disappears before the upper front arrives: $a=0.1$',fontsize=10)
 fig.subplots_adjust(left=.06,right=.98,bottom=.15,top=.9,wspace=.24);fig.savefig('paper-330-settling-fans.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
