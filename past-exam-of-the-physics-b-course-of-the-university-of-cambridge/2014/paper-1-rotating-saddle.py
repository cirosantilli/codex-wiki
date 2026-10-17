"""Original explanatory calculation. Python 3.14, numpy and matplotlib.
Writes one literal PNG basename to cwd; no source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(9.5,4),layout='constrained');w=1.;Om=5.;slow=w*w/(2*Om);M=np.array([[0,0,1,0],[0,0,0,1],[Om*Om-w*w,0,0,2*Om],[0,Om*Om+w*w,-2*Om,0]],float)
e,V=np.linalg.eig(M.astype(complex));coeff=np.linalg.solve(V,np.array([1,0,0,.05-Om]));t=np.linspace(0,4*np.pi/slow,22000);state=(V@(coeff[:,None]*np.exp(e[:,None]*t))).real;x,y=state[:2];X=x*np.cos(Om*t)-y*np.sin(Om*t);Y=x*np.sin(Om*t)+y*np.cos(Om*t)
mask=t<=6*np.pi/Om;a.plot(x[mask],y[mask],lw=1.2);a.scatter([1],[0],color='black',s=22);a.set(title='Rotating axes: first three rotations',xlabel='x (chosen units)',ylabel='y (chosen units)');a.set_aspect('equal')
b.plot(np.cos(slow*t),.5*np.sin(slow*t),color='lightgray',lw=2,label='Leading slow ellipse');b.plot(X,Y,lw=.9,label='Exact laboratory path');b.scatter([1],[0],color='black',s=22);b.set(title='Laboratory: two slow periods',xlabel='X (chosen units)',ylabel='Y (chosen units)');b.set_aspect('equal');b.legend(frameon=False,fontsize=8)
fig.suptitle('Illustration: ω = 1, Ω = 5, initial laboratory position (1,0), velocity (0,0.05)',fontsize=10)
fig.savefig('paper-1-rotating-saddle.png',dpi=150);plt.close(fig)
