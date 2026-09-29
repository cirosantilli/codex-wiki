"""Original sedimentation shock diagrams. Python 3.14; numpy and matplotlib.
Only writes its PNG basename to the output cwd.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def panel(ax,a,zm,triple=False):
 v1=a-1;v2=3*a-1;v3=2*a;t1=zm/(1-a);h1=v3*t1;tf=(1-a-a*zm)/(1-a);hf=a*(1+zm)
 t=np.linspace(0,tf,700);top=1+v1*t;mid=zm+v2*t;bottom=np.where(t<t1,v3*t,h1+a*(t-t1))
 for initial in np.linspace(zm+.025,.975,8):
  z=initial+(2*a-1)*t;low=np.where(t<t1,mid,bottom);mask=(z>low)&(z<top);ax.plot(t[mask],z[mask],color='#d0d9e0',lw=.8)
 for initial in np.linspace(.02,zm-.02,8):
  z=initial+(4*a-1)*t;mask=(t<t1)&(z>v3*t)&(z<mid);ax.plot(t[mask],z[mask],color='#ddd7cf',lw=.8)
 ax.plot(t,top,color='#226ca1',lw=2,label=r'$V_1$');pre=t<=t1+1e-8;ax.plot(t[pre],mid[pre],color='#a16132',lw=2,label=r'$V_2$');ax.plot(t[pre],(v3*t)[pre],color='#29856b',lw=2,label=r'$V_3$')
 if not triple:
  post=t>=t1;ax.plot(t[post],bottom[post],color='#773b93',lw=2,label=r'$V_4$');ax.scatter([t1],[h1],color='black',s=22,zorder=5);ax.annotate(r'$(t_{c1},h_{c1})$',(t1,h1),xytext=(t1-.19,h1+.19),fontsize=10,arrowprops={'arrowstyle':'-','color':'#888888'})
 ax.plot([tf,1.28],[hf,hf],color='#333333',lw=2);ax.scatter([tf],[hf],color='black',s=25,zorder=5);ax.annotate(r'$(t_c,h_c)$' if triple else r'$(t_{c2},h_{c2})$',(tf,hf),xytext=(tf-.27,hf+.25),fontsize=10,arrowprops={'arrowstyle':'-','color':'#888888'})
 ax.axvline(tf,color='#bbbbbb',ls=':',lw=1);ax.axhline(hf,color='#bbbbbb',ls=':',lw=1);ax.text(.035,.98,r'$\phi=a$',fontsize=10,va='top');ax.text(.035,.07,r'$\phi=1$',fontsize=10);ax.text(.88,.83,r'$\phi=0$',fontsize=10);ax.text(.04,zm-.06,r'$\phi=2a$',fontsize=10)
 ax.set(xlim=(0,1.3),ylim=(0,1.03),xlabel=r'$u_st/H$',ylabel='z / H');ax.grid(alpha=.14);ax.legend(fontsize=9,loc='upper right')

def main():
 fig,axes=plt.subplots(1,2,figsize=(10.8,4.7),dpi=100,facecolor='white');panel(axes[0],.2,.5);panel(axes[1],.2,(1-.2)/(1+.2),True);axes[0].set_title(r'Two fronts merge first: $z_m=H/2$');axes[1].set_title('All three fronts meet: tuned layering')
 fig.subplots_adjust(left=.065,right=.975,bottom=.15,top=.90,wspace=.23);fig.savefig('paper-330-compression-shocks.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
