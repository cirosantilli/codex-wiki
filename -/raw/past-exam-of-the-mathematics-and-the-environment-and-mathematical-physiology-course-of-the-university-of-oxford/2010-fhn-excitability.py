"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

a=.15;gamma=2;eps=.001;f=lambda v:v*(a-v)*(v-1)
def field(v,w):return ((f(v)-w)/eps,gamma*v-w)
dt=eps/25;steps=int(1.3/dt);v=.35;w=0;history=[]
for j in range(steps):
 if j%10==0:history.append((j*dt,v,w))
 k1=field(v,w);k2=field(v+dt*k1[0]/2,w+dt*k1[1]/2);k3=field(v+dt*k2[0]/2,w+dt*k2[1]/2);k4=field(v+dt*k3[0],w+dt*k3[1]);v+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6;w+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
hist=np.array(history);fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained');xx=np.linspace(-.4,1.1,500)
axs[0].plot(xx,f(xx),color='.4',label='Cubic nullcline');axs[0].plot(xx,gamma*xx,'--',color='.6',label='Slow nullcline');axs[0].plot(hist[:,1],hist[:,2],label='Excitation trajectory');axs[0].scatter([0,a],[0,0],c=['black','red'],s=25);axs[0].annotate('threshold ≈ a',(a,0),(.15,-.1),arrowprops={'arrowstyle':'->'},fontsize=9);axs[0].set(xlabel='v',ylabel='w',ylim=(-.14,.2),title='Fast jumps and slow cubic-branch motion');axs[0].legend(fontsize=8,loc='upper left');axs[0].text(.63,.007,'fast →',fontsize=8);axs[0].text(.87,.065,'slow ↑',fontsize=8);axs[0].text(.1,.143,'← fast',fontsize=8);axs[0].text(-.25,.04,'slow ↓',fontsize=8)
axs[1].plot(hist[:,0],hist[:,1]);axs[1].set(xlabel='Time',ylabel='v',title='Action potential after a threshold-crossing kick');axs[1].text(.05,.65,'fast rise → slow excursion\n→ fast fall → slow recovery',fontsize=9)
fig.savefig(Path.cwd()/'2010-fhn-excitability.png',dpi=150,facecolor='white');plt.close(fig)
