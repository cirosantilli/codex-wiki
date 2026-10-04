"""Original plot from exam numerical data; Python 3.14, root dependencies."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
age=np.arange(19,41)
ab=np.array([10,92,136,123,317,432,457,540,406,522,529,359,495,540,536,499,518,534,457,459,365,72])
hits=np.array([2,29,37,40,95,139,172,204,128,205,200,134,184,192,173,172,186,199,156,138,105,13])
fitted=1/(1+np.exp(-(-4.5406713+.2684739*age-.0044827*age**2)))
fig,ax=plt.subplots(figsize=(7,4.8),facecolor='white')
ax.scatter(age,hits/ab,s=28,facecolors='white',edgecolors='black',label='Seasonal averages',zorder=3)
ax.plot(age,fitted,color='#2766a8',lw=2,label='Fitted binomial probabilities')
ax.set(xlabel='Age',ylabel='Hits / At Bats',xlim=(18,41),ylim=(.16,.41),title='Quadratic logistic fit to seasonal batting averages')
ax.legend(frameon=False);ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-1-batting-fit.png',dpi=150,facecolor='white')
