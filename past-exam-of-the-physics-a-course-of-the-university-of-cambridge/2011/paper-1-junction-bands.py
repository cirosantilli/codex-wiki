"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(2,2,figsize=(9.5,6.2),layout='constrained');x=np.linspace(-3,3,700)
# Energy zero, gap and band offsets are illustrative and nonquantitative.
for ax,drop,title in zip(axs.flat,[.8,.4,.4,.55],['Equilibrium reference','Rectifier under forward bias','LED: forward injection','Photovoltaic: illumination']):
 ec=1.4-drop*.5*(1+np.tanh(x*1.8));ev=ec-1.0
 ax.axvspan(-.85,.85,color='0.94');ax.plot(x,ec,c='#176493',lw=2);ax.plot(x,ev,c='#176493',lw=2)
 ax.text(-2.85,ec[0]+.05,r'$E_c$');ax.text(-2.85,ev[0]-.15,r'$E_v$')
 ax.text(-2.8,-.68,'p region');ax.text(1.6,-.68,'n region');ax.set(title=title,xlim=(-3.15,3.15),ylim=(-.85,1.95),ylabel='Electron energy (schematic)');ax.set_xticks([]);ax.set_yticks([])
 if title.startswith('Equilibrium'):
  ax.axhline(.5,c='0.3',ls='--',lw=1);ax.text(1.5,.58,r'$E_F$')
 else:
  # Local quasi-Fermi lines only: no claim of a global flat Fermi level.
  ax.plot([-3,-1.2],[.5,.5],'--',c='#9c5a95',lw=1);ax.text(-2.5,.33,r'$E_{Fp}$',color='#9c5a95')
  yn=ec[-1]-.1;ax.plot([1.2,3],[yn,yn],'--',c='#9c5a95',lw=1);ax.text(1.6,yn+.08,r'$E_{Fn}$',color='#9c5a95')
 if title.startswith('Rectifier'):
  ax.annotate('electron injection',xy=(-1,1.55),xytext=(.65,1.55),arrowprops={'arrowstyle':'->'},fontsize=8)
  ax.text(-2.8,1.78,'p positive relative to n',fontsize=8)
 if title.startswith('LED'):
  xpos=.0;i=np.argmin(abs(x-xpos));ax.annotate('',xy=(xpos,ev[i]),xytext=(xpos,ec[i]),arrowprops={'arrowstyle':'->','lw':2,'color':'#b64b24'})
  ax.text(.25,(ec[i]+ev[i])/2,r'$h\nu\approx E_g$',color='#b64b24',fontsize=9)
  ax.text(-2.7,1.78,'Injection → radiative recombination',fontsize=8)
 if title.startswith('Photovoltaic'):
  xpos=0;i=np.argmin(abs(x));ax.annotate('',xy=(xpos,ec[i]),xytext=(xpos,ev[i]),arrowprops={'arrowstyle':'->','lw':2,'color':'#b64b24'})
  ax.text(.2,(ec[i]+ev[i])/2,r'$h\nu\geq E_g$',color='#b64b24',fontsize=9)
  ax.annotate('electrons',xy=(2.5,1.55),xytext=(.5,1.55),arrowprops={'arrowstyle':'->'},fontsize=8)
  ax.annotate('holes',xy=(-2.5,-.4),xytext=(-.4,-.4),arrowprops={'arrowstyle':'->'},fontsize=8)
fig.savefig("paper-1-junction-bands.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
