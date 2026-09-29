#!/usr/bin/env python3
"""Original error-bound sketch. Tested with Python 3.14, matplotlib 3.10.7+dfsg1 (root pin 3.10.7), NumPy 2.3.5.
Run in the desired output directory; saves <this script basename>.png to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
 delta=.002;M=1.;h=np.geomspace(.005,.49,700)
 noise=np.sqrt(6)*delta/h;bias=M*h/2;opt=np.sqrt(2*np.sqrt(6)*delta/M)
 fig,ax=plt.subplots(figsize=(9,5.6),dpi=100,facecolor='white')
 ax.set_facecolor('white');ax.loglog(h,noise,color='#1b679d',lw=2.5,label='Noise bound: √6 δ / h')
 ax.loglog(h,bias,color='#ae5426',lw=2.5,label='Bias bound: M h / 2')
 ax.loglog(h,noise+bias,color='#3b713e',lw=2.8,label='Total upper bound')
 ax.axvline(opt,color='#555555',ls='--',lw=1.2)
 ax.scatter([opt],[np.sqrt(6)*delta/opt+M*opt/2],color='#3b713e',zorder=5)
 ax.annotate('Balance point',xy=(opt,np.sqrt(6)*delta/opt+M*opt/2),xytext=(.19,.32),arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=12)
 ax.set(xlabel='Difference step h (larger h means more smoothing)',ylabel='L² error bound',title='Noise amplification and approximation bias')
 ax.grid(True,which='both',alpha=.18);ax.legend(loc='lower left',fontsize=11)
 ax.text(.99,.02,'Illustration: δ = 0.002, M = 1; bounds, not realized errors',ha='right',va='bottom',transform=ax.transAxes,fontsize=9,color='#444444')
 fig.tight_layout(pad=1.8);fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
