"""Illustrative analytic ROC and corresponding PR curve, not exam measurements."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
tpr=np.linspace(0,1,2001);fpr=tpr**9;prevalence=.1
precision=1/(1+9*tpr**8)
fig,axes=plt.subplots(1,2,figsize=(8.5,4.3),layout='constrained',facecolor='white')
axes[0].plot(fpr,tpr,color='#245c9f',linewidth=2,label='Illustrative classifier: ROC AUC = 0.90')
axes[0].plot([0,1],[0,1],'--',color='.4',label='Uninformative ranking')
axes[0].set(xlabel='False positive rate',ylabel='True positive rate',title='ROC: prevalence-independent ranking')
axes[1].plot(tpr,precision,color='#245c9f',linewidth=2,label='Same classifier; prevalence = 0.10')
axes[1].axhline(prevalence,linestyle='--',color='.4',label='Uninformative precision = prevalence')
axes[1].set(xlabel='Recall',ylabel='Precision',title='Precision–recall: prevalence matters')
for ax in axes:
 ax.set(xlim=(0,1),ylim=(0,1.02));ax.legend(fontsize=8,loc='lower right');ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-4-roc-and-precision.png'),dpi=130,facecolor='white');plt.close(fig)
