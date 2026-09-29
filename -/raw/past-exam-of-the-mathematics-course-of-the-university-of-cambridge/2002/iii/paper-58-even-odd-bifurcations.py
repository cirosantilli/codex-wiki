"""Original diagrams for the even-odd quadratic normal form; output PNG to CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main():
 fig,axes=plt.subplots(1,3,figsize=(11.6,4.2),layout='constrained')
 ax=axes[0];v=np.linspace(-3,3,500);xx,yy=np.meshgrid(v,v)
 ax.contourf(xx,yy,np.where((xx<0)&(yy<0),1,np.nan),levels=[.5,1.5],colors=['#cce5f6'])
 ax.contourf(xx,yy,np.where((xx>0)&(yy<1.6*xx),1,np.nan),levels=[.5,1.5],colors=['#d8edce'])
 ax.contourf(xx,yy,np.where(yy*(xx-.625*yy)>0,1,np.nan),levels=[.5,1.5],colors='none',hatches=['////'])
 ax.axvline(0,color='#7d3c98',lw=1.6);ax.axhline(0,color='#b34b25',lw=1.6);ax.plot(v,1.6*v,color='#b34b25',lw=1.6)
 ax.set(xlim=(-3,3),ylim=(-3,3),xlabel=r'$\lambda_1$',ylabel=r'$\lambda_2$',title='Parameter diagram')
 ax.text(-2,-2,'O stable',ha='center');ax.text(1.7,-2,'P stable',ha='center')
 ax.text(-1.9,1.35,'No stable\nequilibrium',ha='center',fontsize=9)
 ax.text(1.9,2.15,'M exists',rotation=55,fontsize=9);ax.text(-2.1,-1.5,'M exists',rotation=55,fontsize=9)
 ax.text(.08,2.7,'TC',color='#7d3c98',fontsize=8);ax.text(-2.9,.1,'PF at O',color='#b34b25',fontsize=8)
 ax.text(.75,1.9,'PF at P',color='#b34b25',rotation=58,fontsize=8)
 for ax,delta in zip(axes[1:],[1,-1]):
  x=np.linspace(-3,3,1601);stableO=x<min(0,delta);stableP=x>max(0,-5*delta/3)
  for y,st,col in [(0*x,stableO,'#17659d'),(-x,stableP,'#2b7c33')]:
   ax.plot(x,np.where(st,y,np.nan),color=col,lw=2.6)
   ax.plot(x,np.where(~st,y,np.nan),color=col,ls='--',lw=1.8)
  exists=(x-delta)*(3*x+5*delta)>0
  ax.plot(x,np.where(exists,-.625*(x-delta),np.nan),color='#b34b25',ls='--',lw=2)
  for z in [delta,-5*delta/3,0]:ax.axvline(z,color='.8',lw=.7)
  ax.scatter([delta,-5*delta/3,0],[0,5*delta/3,0],s=27,facecolor='white',edgecolor='black',zorder=5)
  ax.set(xlim=(-3,3),ylim=(-3,3),xlabel=r'$\lambda_1/|\Delta|$',ylabel=r'$aA/|\Delta|$',title=r'$\Delta '+('>0' if delta>0 else '<0')+'$')
  ax.text(1.8,.12,'O',color='#17659d');ax.text(1.9,-2.5,'P',color='#2b7c33');ax.annotate('M± (same A)',xy=(-2.5,-.625*(-2.5-delta)),xytext=(-2.85,1.5 if delta>0 else 1.85),color='#b34b25',fontsize=8,arrowprops={'arrowstyle':'->','color':'#b34b25','lw':.8})
  ax.grid(alpha=.15)
 fig.legend(handles=[Line2D([],[],color='black',lw=2.4,label='stable'),Line2D([],[],color='black',ls='--',label='unstable'),Line2D([],[],color='#7d3c98',label='TC: transcritical'),Line2D([],[],color='#b34b25',label='PF: pitchfork')],loc='outside lower center',ncol=4,frameon=False,fontsize=9)
 fig.savefig('paper-58-even-odd-bifurcations.png',dpi=130,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
