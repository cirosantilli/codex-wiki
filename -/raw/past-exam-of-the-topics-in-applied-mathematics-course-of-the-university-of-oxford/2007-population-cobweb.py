# Tested with Python3.14.4,numpy2.3.5,matplotlib3.10.7. Writes PNG to CWD.
import numpy as np
import matplotlib.pyplot as plt
f=lambda x:x/(2+x*x)
x=np.linspace(0,2.4,500);fig,ax=plt.subplots(figsize=(6,5),facecolor='white');ax.plot(x,f(x),label=r'$F(u)=u/(2+u^2)$');ax.plot(x,x,'--',color='gray',label='$F(u)=u$');u=2.2;y=0
for i in range(13):
 v=f(u);ax.plot([u,u,v],[y,v,v],color='#bd4328',lw=1.5);u=v;y=v
ax.set(xlim=(0,2.4),ylim=(0,2.4),xlabel='$u_n$',ylabel='$u_{n+1}$',title='Cobweb approaches extinction');ax.legend();ax.grid(alpha=.18);fig.tight_layout()
fig.savefig('2007-population-cobweb.png',dpi=160,facecolor='white')
