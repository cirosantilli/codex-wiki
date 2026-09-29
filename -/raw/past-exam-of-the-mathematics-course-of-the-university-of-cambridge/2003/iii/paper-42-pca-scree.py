"""Derived PCA variance sketch; emit one PNG to caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Caller controls MPLCONFIGDIR; only declared root dependencies are used.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

covariance=np.array([[.05458445,.01061861,.12008415],[.01061861,.00734844,.02926209],[.12008415,.02926209,.27695632]])
eigenvalues=np.linalg.eigvalsh(covariance)[::-1]*(30/31)
fractions=eigenvalues/eigenvalues.sum()
fig,axes=plt.subplots(1,2,figsize=(8.4,3.8),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.set_xticks([1,2,3])
    ax.set_xlabel('Principal component')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',color='#dddddd',lw=.6)
axes[0].plot([1,2,3],eigenvalues,'o-',color='#244d73',lw=2)
axes[0].set_ylim(0,.35)
axes[0].set_ylabel('Variance (divisor 31)')
axes[0].set_title('Scree plot')
for i,(value,fraction) in enumerate(zip(eigenvalues,fractions),1):
    axes[0].annotate(f'{100*fraction:.3f}%',(i,value),xytext=(0,8),textcoords='offset points',ha='center',fontsize=9)
axes[1].plot([1,2,3],100*np.cumsum(fractions),'o-',color='#9a4e16',lw=2)
axes[1].set_ylim(97.5,100.35)
axes[1].set_ylabel('Cumulative explained variance (%)')
axes[1].set_title('Variance retained')
axes[1].set_yticks([98,99,100])
fig.tight_layout()
fig.savefig('paper-42-pca-scree.png',facecolor='white',transparent=False)
plt.close(fig)
