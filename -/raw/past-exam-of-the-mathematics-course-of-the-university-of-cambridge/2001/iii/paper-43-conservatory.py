"""Original hydraulic sketches, computed from a common Bernoulli head. Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7. CWD-only PNG output."""
import numpy as np
import matplotlib.pyplot as plt
q=.22;x=np.linspace(0,6,601);first=2.;second=4.5

def geometry(xx,W2):
 g1=np.exp(-((xx-first)/.32)**2);g2=np.exp(-((xx-second)/.32)**2)
 return 1.7-.5*g1-.5*g2,3.-2.*g1-(3.-W2)*g2

def root(e,W,branch):
 hc=(q*q/W**2)**(1/3)
 if e<1.5*hc-1e-9:raise ValueError('head below a local critical minimum')
 e=max(e,1.5*hc);lo,hi=(1e-8,hc) if branch=='thin' else (hc,e+1)
 for _ in range(65):
  mid=(lo+hi)/2;value=mid+q*q/(2*W*W*mid*mid)
  if branch=='thin':
   if value>e:lo=mid
   else:hi=mid
  else:
   if value>e:hi=mid
   else:lo=mid
 return (lo+hi)/2

def critical(at,W2):
 H,W=geometry(at,W2);return 1.5*(q*q/W**2)**(1/3)-H

def loss(at,E,W2):
 H,W=geometry(at,W2);h1=root(E+H,W,'thin');Fr2=q*q/(W*W*h1**3);h2=h1*(np.sqrt(1+8*Fr2)-1)/2
 return (h2-h1)**3/(4*h1*h2)
fig,axs=plt.subplots(2,2,figsize=(12,6.4),facecolor='white')
def draw(ax,W2,mode,title):
 H,W=geometry(x,W2);E1=critical(first,W2);E2=critical(second,W2);jump=None
 if mode=='first':
  E=np.full_like(x,E1);branches=['thick' if xx<first else 'thin' for xx in x]
 elif mode=='second':
  E=np.full_like(x,E2);branches=['thick' if xx<second else 'thin' for xx in x]
 else:
  target=E1-E2;lo=first+1e-5;hi=3.1
  assert loss(lo,E1,W2)<target<loss(hi,E1,W2)
  for _ in range(65):
   mid=(lo+hi)/2
   if loss(mid,E1,W2)>target:hi=mid
   else:lo=mid
  jump=(lo+hi)/2;E=np.where(x<jump,E1,E2);branches=['thick' if xx<first or jump<=xx<second else 'thin' for xx in x]
 h=np.array([root(e+HH,WW,br) for e,HH,WW,br in zip(E,H,W,branches)])
 ax.fill_between(x,H-h,H,color='#f2c4a2');ax.plot(x,H,color='black',lw=2);ax.plot(x,H-h,color='#9e572e',lw=2);ax.axvline(first,color='#808080',ls=':',lw=1);ax.axvline(second,color='#808080',ls=':',lw=1);ax.text(.15,1.84,'room',fontsize=9);ax.text(2.65,1.84,'conservatory',fontsize=9);ax.text(4.97,1.84,'outside',fontsize=9);ax.text(first,.55,'W1',ha='center',fontsize=9);ax.text(second,.55,'W2',ha='center',fontsize=9)
 controls=[first] if mode=='first' else [second] if mode=='second' else [first,second]
 for at in controls:
  HH,WW=geometry(at,W2);hc=(q*q/WW**2)**(1/3);ax.scatter([at],[HH-hc],color='#c85b21',s=25);ax.annotate('F = 1',xy=(at,HH-hc),xytext=(at-.55,1.04),arrowprops={'arrowstyle':'->'},fontsize=8)
 if jump is not None:
  idx=int(np.argmin(abs(x-jump)));ax.annotate('jump',xy=(jump,H[idx]-h[idx]),xytext=(jump+.35,1.18),arrowprops={'arrowstyle':'->'},fontsize=9)
 ax.set(xlim=(0,6),ylim=(.5,1.98),title=title,xlabel='distance downstream (schematic geometry)',ylabel='height');return jump

draw(axs[0,0],1.6,'first','W2 > W1: first control, supercritical passage')
draw(axs[0,1],1.6,'both','W2 > W1: a jump can feed a second control')
draw(axs[1,0],.7,'second','W2 < W1: downstream control backs up the first')
axs[1,1].axis('off');axs[1,1].text(.04,.88,'Same doorway heights and conserved buoyancy\n\nNarrower throat = larger critical head\n\nW2 = W1: marginal equal critical heads;\npositive jump losses prevent two free controls\n\nMixing, roof height and losses can change selection.\nRelative width does not locate a jump uniquely.',va='top',fontsize=11)
fig.tight_layout();fig.savefig('paper-43-conservatory.png',dpi=120,facecolor='white');plt.close(fig)
