"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axs=plt.subplots(1,3,figsize=(13,3.6),layout='constrained')
T=np.linspace(.7,1.25,500)
for mu in (3,12):axs[0].plot(T,(2-np.tanh(mu*(T**4-1)))/4,label=fr'$\mu={mu}$')
axs[0].set(xlabel=r'$T/T_0$',ylabel='Albedo',title='Smooth ice-albedo transition',ylim=(.2,.8));axs[0].legend()
s=np.linspace(0,2,1000);v=np.empty(len(s));v[0]=1.5**.25;dt=s[1]-s[0]
f=lambda x:1-x**4
for j in range(len(s)-1):
 k1=f(v[j]);k2=f(v[j]+dt*k1/2);k3=f(v[j]+dt*k2/2);k4=f(v[j]+dt*k3);v[j+1]=v[j]+dt*(k1+2*k2+2*k3+k4)/6
axs[1].plot(s,v);axs[1].axhline(1,color='.6',ls=':');axs[1].set(xlabel=r'Fast time $t/\varepsilon$',ylabel=r'$T/T_0$',title='Initial cooling; frozen albedo')
t=np.linspace(0,5,400);axs[2].plot(t,((3-np.exp(-t))/2)**.25,label='Temperature');axs[2].set(xlabel='Slow time t',ylabel=r'$T/T_0$',title='Sharp-transition outer recovery');axs[2].axhline(1.5**.25,color='.6',ls=':');axs[2].text(.15,1.075,'After fast layer;\npossible finite-μ delay omitted',fontsize=8)
fig.savefig(Path.cwd()/'2010-climate-feedback.png',dpi=150,facecolor='white');plt.close(fig)
