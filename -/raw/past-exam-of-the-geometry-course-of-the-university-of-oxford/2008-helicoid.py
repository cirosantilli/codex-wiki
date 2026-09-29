"""Original helicoid figure; Python3.14/numpy/matplotlib; output in CWD."""
import numpy as np
import matplotlib.pyplot as plt
u,v=np.meshgrid(np.linspace(-np.pi,np.pi,100),np.linspace(-1.3,1.3,33))
x,y,z=v*np.cos(u),v*np.sin(u),u
fig=plt.figure(figsize=(6.4,5.2),facecolor='white',layout='constrained')
ax=fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z,cmap='viridis',alpha=.82,linewidth=0,antialiased=True)
for angle in np.linspace(-np.pi,np.pi,9):
    r=np.linspace(-1.3,1.3,40)
    ax.plot(r*np.cos(angle),r*np.sin(angle),np.full_like(r,angle),color='#21334d',lw=1)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Helicoid: straight rulings, zero mean curvature')
ax.set_box_aspect((2.6,2.6,5.5));ax.view_init(elev=22,azim=-58)
fig.savefig('2008-helicoid.png',dpi=150,facecolor='white',bbox_inches='tight',pad_inches=.25)
