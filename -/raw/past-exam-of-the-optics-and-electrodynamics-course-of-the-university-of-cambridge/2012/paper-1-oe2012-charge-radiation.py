import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6.4,5.4),layout='constrained');ax=fig.add_subplot(projection='polar')
theta=np.linspace(0,2*np.pi,1000);power=np.sin(theta)**2
ax.set_theta_zero_location('N');ax.set_theta_direction(-1)
ax.plot(theta,power,color='#2475aa',lw=2.5);ax.fill(theta,power,color='#2475aa',alpha=.12)
ax.set_rticks([.25,.5,.75,1]);ax.set_rlabel_position(135);ax.set_ylim(0,1.12)
ax.set_thetagrids([0,45,90,135,180,225,270,315]);ax.grid(alpha=.35)
ax.set_title(r'Normalized $dP/d\Omega=\sin^2\vartheta$'+'\n'+r'Acceleration points along the $0^\circ$ axis',pad=22)
fig.savefig('paper-1-oe2012-charge-radiation.png',dpi=160,facecolor='white')
