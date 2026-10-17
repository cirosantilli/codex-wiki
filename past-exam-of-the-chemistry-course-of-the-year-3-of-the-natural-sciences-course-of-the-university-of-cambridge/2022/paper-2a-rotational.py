"""Original solution figure. Tested with Python 3.14, numpy and matplotlib.
The PNG basename is written to the current working directory for Make's _media target.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, flow, finish, save

fig,axs=plt.subplots(1,2,figsize=(10,3.8))
for a,J,vals in [(axs[0],2,[1.50130,1.50128,1.50122]),(axs[1],3,[2.00171,2.00168,2.00160,2.00147])]:
 shift=(np.array(vals)-vals[0])*1e5
 for K,x in enumerate(shift):
  a.vlines(x,0,1,color='#245c9f',lw=2);a.text(x,1.06,f'K = {K}',rotation=45,ha='left',fontsize=11)
  a.text(x,-.1,f'{vals[K]:.5f}',rotation=45,ha='right',va='top',fontsize=9)
 a.set(xlim=(min(shift)-4,4),ylim=(-.5,1.6),yticks=[],xlabel=r'Shift from K = 0 ($10^{-5}$ cm$^{-1}$)',title=f'J = {J} → {J+1}')
 for sp in ['top','right','left']:a.spines[sp].set_visible(False)
 a.text(.04,.87,'Derived assignments\n+K and −K coincident',transform=a.transAxes,fontsize=10)
fig.tight_layout();save(fig,'paper-2a-rotational.png')
