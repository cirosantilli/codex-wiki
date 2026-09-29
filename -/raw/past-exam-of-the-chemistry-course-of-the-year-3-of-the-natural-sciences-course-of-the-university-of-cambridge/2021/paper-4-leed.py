"""Original explanatory diagram; Python 3.14 with numpy and matplotlib.
The PNG basename is written to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(6.5,6.3),layout='constrained');g=4*np.pi/(np.sqrt(3)*3.84);k=np.sqrt(50/3.809982116);limit=k*np.sin(np.deg2rad(75))
for h in range(-3,4):
 for l in range(-3,4):
  q=g*np.array([h+l/2,np.sqrt(3)*l/2]);inside=np.linalg.norm(q)<limit
  if np.linalg.norm(q)<4.3:
   ax.scatter(*q,s=65 if inside else 25,c=BLUE if inside else '.75');
   if inside:ax.text(q[0]+.08,q[1]+.08,f'({h},{l})',fontsize=9)
ax.add_patch(Circle((0,0),limit,fill=False,ec=ORANGE,lw=1.6,label='screen cutoff k sin 75°'));ax.add_patch(Circle((0,0),k,fill=False,ec='.6',ls='--',label='propagation limit k'))
ax.set(xlim=(-4.2,4.2),ylim=(-4.2,4.2),xlabel='Parallel reciprocal component (Å⁻¹)',ylabel='Parallel reciprocal component (Å⁻¹)',title='12 off-axis beams plus the specular beam');ax.set_aspect('equal');ax.legend(loc='upper center',fontsize=9)
save(fig,'paper-4-leed.png')
