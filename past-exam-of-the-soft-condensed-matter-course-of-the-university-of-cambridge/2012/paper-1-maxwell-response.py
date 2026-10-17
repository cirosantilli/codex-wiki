"""Original Maxwell storage/loss calculation, normalized by spring modulus."""
import numpy as np
import matplotlib.pyplot as plt

def main():
 plt.rcParams.update({'font.size':10})
 x=np.logspace(-3,3,600);gp=x*x/(1+x*x);gpp=x/(1+x*x)
 fig,ax=plt.subplots(figsize=(6.1,3.8),layout='constrained')
 ax.loglog(x,gp,label=r'Storage $G^\prime/G_0$',lw=2);ax.loglog(x,gpp,label=r'Loss $G^{\prime\prime}/G_0$',lw=2)
 ax.scatter([1],[.5],c='black',s=25,zorder=5);ax.axvline(1,c='.6',ls=':',lw=1);ax.text(1.25,.6,'Both = 1/2',fontsize=9)
 ax.set(xlabel=r'$\omega\tau$',ylabel='Normalized modulus',ylim=(1e-6,2),title='Slow flow and fast elastic response');ax.legend(fontsize=9,loc='lower right');ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
 fig.savefig('paper-1-maxwell-response.png',dpi=170,facecolor='white');plt.close(fig)
if __name__=='__main__':main()
