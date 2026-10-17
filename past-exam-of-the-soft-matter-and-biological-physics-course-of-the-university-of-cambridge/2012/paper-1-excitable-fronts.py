"""Original generic cubic-front profiles and fast-slow phase trajectory."""
import numpy as np
import matplotlib.pyplot as plt

def local_rhs(y,alpha=.2,beta=1.,eps=.01):
 u,w=y;return np.array([u*(1-u)*(u-alpha)-w,eps*(u-beta*w)])
def trajectory(T=450.,dt=.02):
 out=np.empty((round(T/dt)+1,2));out[0]=[.65,0]
 for j in range(len(out)-1):
  y=out[j];k1=local_rhs(y);k2=local_rhs(y+dt*k1/2);k3=local_rhs(y+dt*k2/2);k4=local_rhs(y+dt*k3);out[j+1]=y+dt*(k1+2*k2+2*k3+k4)/6
 return out

def main():
 plt.rcParams.update({'font.size':10})
 fig,ax=plt.subplots(1,2,figsize=(8.5,3.9),layout='constrained');x=np.linspace(-12,16,700);alpha=.2;speed=np.sqrt(.5)*(1-2*alpha)
 for t in [0.,8.,16.]:ax[0].plot(x,1/(1+np.exp((x-speed*t)/np.sqrt(2))),lw=1.8,label=f't = {t:g}')
 ax[0].set(xlabel='x (dimensionless)',ylabel='u',title='Frozen recovery: advancing cubic front');ax[0].legend(fontsize=8)
 u=np.linspace(-.3,1.1,500);ax[1].plot(u,u*(1-u)*(u-.2),'--',c='#44844c',label='Fast nullcline');ax[1].plot(u,u,':',c='#8b668e',label='Slow nullcline')
 tr=trajectory();ax[1].plot(tr[:,0],tr[:,1],c='#286e9c',lw=1.4,label='One finite perturbation')
 for j in [100,1700,4500]:ax[1].annotate('',tr[j+25],tr[j],arrowprops={'arrowstyle':'->','color':'#286e9c','lw':1.3})
 ax[1].scatter([0],[0],c='black',s=25,zorder=5);ax[1].scatter([tr[0,0]],[tr[0,1]],facecolor='white',edgecolor='#286e9c',s=25,zorder=5)
 ax[1].set(xlim=(-.38,1.1),ylim=(-.03,.21),xlabel='Fast variable u',ylabel='Slow feedback w',title='Generic excitation and recovery');ax[1].legend(fontsize=7,loc='upper left')
 for p in ax:p.grid(alpha=.16);p.spines[['top','right']].set_visible(False)
 fig.suptitle(r'Illustrative nondimensional $D=1$, $\alpha=0.2$, $\beta=1$, $\varepsilon=0.01$; no biological variables',fontsize=9)
 fig.savefig('paper-1-excitable-fronts.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
