"""Original monochromatic and polychromatic single-slit plots.
Python 3.14, NumPy, Matplotlib; PNG basename is written to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
slit=30e-6; wave=500e-9
fig,axes=plt.subplots(2,2,figsize=(9.6,6.5),layout='constrained')
for ax,d,scale,title in [(axes[0,0],6.,1.,'Original screen, 6 m'),(axes[0,1],.1,1000.,'Compressed screen, 0.10 m')]:
 y=np.linspace(-3*d*wave/slit,3*d*wave/slit,3001);intensity=np.sinc(slit*y/(d*wave))**2
 ax.plot(y*scale,intensity,color='#254c8a',lw=1.7)
 for sign in [-1,1]:ax.axvline(sign*d*wave/slit*scale,color='0.45',ls='--',lw=.9)
 ax.set(xlabel='Screen position ('+('m' if scale==1 else 'mm')+')',ylabel=r'$I/I(0)$',title=title,ylim=(-.025,1.05))
 ax.text(.99,.87,'First zeros: '+('±0.100 m' if scale==1 else '±1.67 mm'),ha='right',transform=ax.transAxes,fontsize=9)
u=np.linspace(0,4,4001)
for ax,title in [(axes[1,0],'Different colours share the centre'),(axes[1,1],'No common first dark fringe: expanded scale')]:
 for wavelength,color in [(450e-9,'#2465d7'),(500e-9,'#168c62'),(650e-9,'#c23b35')]:
  ax.plot(u,np.sinc(u*wave/wavelength)**2,color=color,label=f'{wavelength*1e9:.0f} nm',lw=1.6)
 ax.axvline(1,color='0.4',ls=':',lw=.9)
 ax.set(xlabel=r'$a\theta/\lambda_0$ ($\lambda_0=500$ nm)',ylabel=r'$I_\lambda/I_\lambda(0)$',title=title)
 ax.legend(fontsize=8)
axes[1,0].set(xlim=(0,2),ylim=(-.02,1.05));axes[1,1].set(xlim=(.7,3.5),ylim=(0,.17))
fig.suptitle('Calculated narrow-slit diffraction; ideal thin lens and paraxial approximation',fontsize=12)
fig.savefig('paper-1-ia2013-slit-patterns.png',dpi=140,facecolor='white')
