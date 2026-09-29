"""Original Flory-Huggins model and concentration crossover diagram."""
import numpy as np
import matplotlib.pyplot as plt

def free_energy(phi,chi,N):
 return phi*np.log(phi)/N+(1-phi)*np.log1p(-phi)+chi*phi*(1-phi)
def coexistence(chi,N):
 # Lower convex envelope: its longest missing interval brackets the binodal.
 x=np.unique(np.r_[np.geomspace(1e-35,.025,5500),np.linspace(.025,.999999,4500)])
 y=free_energy(x,chi,N);h=[]
 for j in range(len(x)):
  while len(h)>1:
   i,k=h[-2],h[-1]
   if (y[k]-y[i])/(x[k]-x[i]) < (y[j]-y[k])/(x[j]-x[k]):break
   h.pop()
  h.append(j)
 gaps=np.diff(h);i=int(np.argmax(gaps));return float(x[h[i]]),float(x[h[i+1]])
def main():
 plt.rcParams.update({'font.size':9})
 N=1e4;pc=1/(1+np.sqrt(N));cc=.5*(1+N**(-.5))**2
 chis=np.linspace(cc+1e-4,.65,110);pairs=np.array([coexistence(c,N) for c in chis])
 fig,ax=plt.subplots(figsize=(8.3,5.3),layout='constrained')
 ax.fill_betweenx(chis,np.maximum(pairs[:,0],1e-5),pairs[:,1],color='#e9b6b7',alpha=.6)
 ax.plot(pairs[:,0],chis,c='#b93339',lw=1.7,label='Model binodal');ax.plot(pairs[:,1],chis,c='#b93339',lw=1.7)
 p=np.geomspace(1e-5,.999,2500);cs=.5*(1/(N*p)+1/(1-p));ax.plot(p,cs,'--',color='#99595e',lw=.8,label='Model spinodal')
 goodchi=np.linspace(0,.5,501);overlap=N**(-.8)*np.maximum(1-2*goodchi,N**(-.5))**(-.6)
 ax.plot(overlap,goodchi,color='#2d9661',lw=2,label='Overlap crossover (scaling)')
 ax.axhline(.5,c='.4',ls=':',lw=1);ax.scatter([pc],[cc],s=28,c='black',zorder=5)
 ax.annotate('Finite-chain critical point',(pc,cc),(.025,.55),arrowprops={'arrowstyle':'->'},fontsize=8)
 ax.text(1.4e-5,.478,r'$\theta:\ \chi=1/2$',fontsize=9)
 ax.text(1e-4,.23,'Dilute coils',ha='center',color='#267148')
 ax.text(.022,.23,'Semidilute',ha='center',color='#267148')
 ax.text(.62,.23,'Concentrated\n(near unity)',ha='center',fontsize=9)
 ax.text(.003,.61,'Two phases',ha='center',color='#8d262e')
 ax.text(1.5e-5,.055,'Good solvent',fontsize=10);ax.text(1.5e-5,.635,'Poor-solvent side',fontsize=9)
 ax.set(xscale='log',xlim=(1e-5,1),ylim=(0,.65),xlabel=r'Polymer volume fraction $\phi$',ylabel=r'Interaction parameter $\chi$',title=r'Illustrative $N=10^4$: crossovers and phase separation differ')
 ax.legend(loc='lower right',fontsize=8);ax.spines[['top','right']].set_visible(False)
 fig.savefig('paper-1-polymer-regimes.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
