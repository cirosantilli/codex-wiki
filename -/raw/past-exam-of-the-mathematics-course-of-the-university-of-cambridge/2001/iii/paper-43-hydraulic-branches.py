"""Original computed hydraulic profiles; Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7; CWD output."""
import numpy as np
import matplotlib.pyplot as plt
q=.42**1.5;hc=q**(2/3);x=np.linspace(-2.5,2.5,480);roof=2.2-.4*np.exp(-(x/.65)**2);Ec=1.5*hc-1.8

def depth(e,branch):
 minimum=1.5*hc
 if e<minimum-1e-10:raise ValueError('inaccessible energy')
 e=max(e,minimum)
 lo,hi=(1e-7,hc) if branch=='thin' else (hc,e+1)
 for _ in range(65):
  m=(lo+hi)/2;value=m+q*q/(2*m*m)
  if branch=='thin':
   if value>e:lo=m
   else:hi=m
  else:
   if value>e:hi=m
   else:lo=m
 return (lo+hi)/2

def profile(E,branches):return np.array([depth(E+H,b) for H,b in zip(roof,branches)])
fig,axs=plt.subplots(2,3,figsize=(12,6.5),facecolor='white');a=axs[0,0];hh=np.linspace(.12,1.35,350);ee=hh+q*q/(2*hh*hh);a.plot(hh,ee,color='#1d608c');a.axhline(1.5*hc,color='#c05b2b',ls='--',label='critical minimum');a.axhline(1.5*hc+.18,color='gray',ls=':');a.axvline(hc,color='gray',ls=':');a.text(.16,1.25,'supercritical');a.text(.66,.86,'subcritical');a.set(xlabel='layer depth h',ylabel='available head E + roof height',ylim=(.5,1.5),title='Two branches of the energy curve');a.legend(fontsize=8)
def draw(ax,h,title):
 ax.fill_between(x,roof-h,roof,color='#f3c7a7');ax.plot(x,roof,color='black',lw=2);ax.plot(x,roof-h,color='#a35d2c',lw=2);ax.annotate('',xy=(2.05,2.33),xytext=(1.3,2.33),arrowprops={'arrowstyle':'->'});ax.text(-2.4,2.35,'light layer below roof',fontsize=8);ax.set(xlim=(-2.5,2.5),ylim=(.8,2.45),title=title,xlabel='distance downstream',ylabel='height')
draw(axs[0,1],profile(Ec+.18,['thick']*len(x)),'Subcritical passage: head above threshold')
draw(axs[0,2],profile(Ec+.18,['thin']*len(x)),'Supercritical passage: head above threshold')
controlled=profile(Ec,['thick' if z<0 else 'thin' for z in x]);draw(axs[1,0],controlled,'Critical crest: subcritical to supercritical');axs[1,0].scatter([0],[1.8-hc],color='#c05b2b');axs[1,0].text(.1,1.2,'F = 1',fontsize=9)
xj=1.05;Hj=2.2-.4*np.exp(-(xj/.65)**2);h1=depth(Ec+Hj,'thin');Fr2=q*q/h1**3;h2=h1*(np.sqrt(1+8*Fr2)-1)/2;loss=(h2-h1)**3/(4*h1*h2);Eafter=Ec-loss
jump=np.array([depth((Ec if z<xj else Eafter)+H,'thick' if z<0 or z>=xj else 'thin') for z,H in zip(x,roof)]);draw(axs[1,1],jump,'Controlled outflow followed by a hydraulic jump');axs[1,1].annotate('jump: head loss',xy=(xj,Hj-(h1+h2)/2),xytext=(.35,.9),arrowprops={'arrowstyle':'->'},fontsize=9)
a=axs[1,2];a.axis('off');a.text(.03,.8,'Roof depression = inverted weir\n\nF < 1: information can return upstream\nF > 1: both characteristics go downstream\n\nBelow the crest energy minimum:\nno smooth steady flow at the specified flux\n\nA jump conserves mass and momentum,\nbut loses energy.',va='top',fontsize=10)
fig.tight_layout();fig.savefig('paper-43-hydraulic-branches.png',dpi=120,facecolor='white');plt.close(fig)
