"""Original phase portraits. Output CWD; Python3.14.4/numpy2.3.5/matplotlib3.10.7.
Shooting constants are obtained from the stated oscillator and its variational equation.
Each file generates only its basename-matched PNG.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ah=.33144619340593945;af=.3314706632638702;am=(ah+af)/2

def trace(a,x,y,T,dt=.0005):
 out=[(x,y)]
 def f(x,y):return y,x*x*x-x+a*y-y*y*y
 for i in range(int(T/dt)):
  p,q=f(x,y);r,s=f(x+dt*p/2,y+dt*q/2);t,u=f(x+dt*r/2,y+dt*s/2);v,w=f(x+dt*t,y+dt*u)
  x+=dt*(p+2*r+2*t+v)/6;y+=dt*(q+2*s+2*u+w)/6;out.append((x,y))
  if abs(x)>1.7 or abs(y)>2:break
 return np.asarray(out)
fig,axes=plt.subplots(2,3,figsize=(11,7),layout='constrained',facecolor='white')
cases=[(-.3,'A>0: attracting origin'),(.2,'Small −A: attracting cycle'),(ah,'a=ah: repelling saddle loop'),(am,'ah<a<af: two cycles'),(af,'a=af: semistable cycle'),(.6,'a>af: escape')]
xx=np.linspace(-1.35,1.35,75);yy=np.linspace(-1.35,1.35,75);X,Y=np.meshgrid(xx,yy)
for ax,(a,title) in zip(axes.flat,cases):
 U=Y;V=X**3-X+a*Y-Y**3;speed=np.hypot(U,V);ax.streamplot(xx,yy,U/(speed+.04),V/(speed+.04),color='#b4bdc4',density=.65,linewidth=.6,arrowsize=.7)
 ax.scatter([-1,1],[0,0],s=30,color='black',marker='x',zorder=4);ax.scatter([0],[0],s=20,color='black',zorder=4);ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35),xlabel='x=z',ylabel='y=dz/dt',title=title);ax.set_aspect('equal');ax.set_facecolor('white')
 if a==.2:
  p=trace(a,.2,0,130,.001)[60000:];ax.plot(p[:,0],p[:,1],color='#176b9b',lw=1.7)
 if a==ah:
  p=trace(a,0,.6870814856922773,22);ax.plot(p[:,0],p[:,1],color='#176b9b',lw=1.6)
  eps=1e-7;rate=(a+np.sqrt(a*a+8))/2;conn=trace(a,-1+eps,rate*eps,35);mask=(conn[:,0]<.99995)&(conn[:,1]>=0);conn=conn[mask];ax.plot(conn[:,0],conn[:,1],color='#ba4a38',ls='--',lw=1.4);ax.plot(-conn[:,0],-conn[:,1],color='#ba4a38',ls='--',lw=1.4)
 if a==am:
  inn=trace(a,0,.6871639514598494,15.6876676283);outer=trace(a,0,.6874616726766689,19.1614424658)
  ax.plot(inn[:,0],inn[:,1],color='#176b9b',lw=1.6);ax.plot(outer[:,0],outer[:,1],color='#ba4a38',ls='--',lw=1.3)
  inset=ax.inset_axes([.53,.08,.43,.26]);inset.plot(inn[:,0],inn[:,1],color='#176b9b');inset.plot(outer[:,0],outer[:,1],color='#ba4a38',ls='--');inset.set(xlim=(-.008,.008),ylim=(.687,.68765));inset.tick_params(labelsize=6);inset.set_title('Two crossings: zoom',fontsize=7)
 if a==af:
  p=trace(a,0,.6873357061564271,16.77487547765);ax.plot(p[:,0],p[:,1],color='#8c4f99',lw=1.8)
fig.suptitle('Softening oscillator: a=−A; blue attracts, dashed red repels',fontsize=12)
fig.savefig('2011-softening-phase-portraits.png',dpi=135,facecolor='white');plt.close(fig)
