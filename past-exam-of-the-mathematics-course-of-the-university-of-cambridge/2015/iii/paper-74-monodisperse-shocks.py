"""Original settling diagram; output PNG basename to cwd.
Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.paper-74-mplconfig'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
 fig,ax=plt.subplots(figsize=(9,6),dpi=100,facecolor='white');ax.set_facecolor('white')
 t=np.linspace(0,1,120);lower=t/8;upper=1-7*t/8
 ax.fill_betweenx(t,0,lower,color='#bc956b',alpha=.65);ax.fill_betweenx(t,lower,upper,color='#b8d8ed',alpha=.65);ax.fill_betweenx(t,upper,1,color='#f7fbfc')
 ax.plot(upper,t,c='#286b96',lw=2.5,label='Clearing front');ax.plot(lower,t,c='#8b5933',lw=2.5,label='Deposit front')
 ax.plot([.125,.125],[1,1.2],c='#8b5933',lw=2.5);ax.plot(.125,1,'ko',ms=5)
 ax.text(.62,.18,'Clear fluid',ha='center');ax.text(.39,.48,r'Suspension: $\phi/\phi_{\max}=1/8$',fontsize=11,ha='center');ax.text(.05,.61,'Deposit',rotation=90,ha='center',va='center',fontsize=10)
 ax.annotate(r'$(h_c/H,W_st_c/H)=(1/8,1)$',xy=(.125,1),xytext=(.3,1.12),arrowprops={'arrowstyle':'-','color':'#555'},fontsize=11)
 ax.set_xlim(0,1);ax.set_ylim(0,1.25);ax.set_xlabel('Height above bottom, $z/H$');ax.set_ylabel('Time, $W_s(a)t/H$');ax.legend(loc='upper right',fontsize=10)
 ax.set_title('Monodisperse batch settling: clearing and growing deposit',fontsize=14)
 fig.tight_layout();fig.savefig(Path.cwd()/'paper-74-monodisperse-shocks.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
