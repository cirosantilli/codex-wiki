"""Original best-response/tie diagram for a discrete three-firm location game.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG to CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k, c = 9, 4

def payoff(s, z):
    sites = (c, s, z)
    result = [0, 0, 0]
    for customer in range(1, k+1):
        distances = [abs(customer-site) for site in sites]
        winners = [i for i,d in enumerate(distances) if d == min(distances)]
        for i in winners:
            result[i] += 2 // len(winners)
    return result

outcomes = {}
for s in range(1, k+1):
    if s == c:
        continue
    legal = [(z, payoff(s,z)) for z in range(1,k+1) if z not in (c,s)]
    best = max(v[2] for z,v in legal)
    outcomes[s] = [(z,v) for z,v in legal if v[2] == best]
assert outcomes[6] == [(3,[3,9,6]),(7,[9,3,6])]
assert outcomes[7] == [(3,[4,8,6])]

fig, ax = plt.subplots(figsize=(8,4.6), dpi=110, facecolor='white')
ax.set_facecolor('white')
ax.axvspan(8,10, color='#e4f1e8', zorder=0)
ax.axvline(8, color='#377148', ls='--', lw=1.4)
ax.axhline(2, color='#9a3d30', ls=':', lw=1.4, label='C payoff after a central opening')
for s, options in outcomes.items():
    for z,v in options:
        x,y = v[1],v[0]
        ax.scatter(x,y,s=45,color='#8d959a',zorder=3)
        if s != 6:
            ax.annotate(f'S = {s}',(x,y),xytext=(5,7),textcoords='offset points',fontsize=10,color='#566168')
# Mixing between N's two best replies at S=6 traces this segment.
x=np.linspace(3,9,121)
ax.plot(x,12-x,color='#8a9db3',lw=1.7,label='N tie mixtures after S = 6')
x_good=np.linspace(8,9,31)
ax.plot(x_good,12-x_good,color='#17658a',lw=4,zorder=4)
ax.scatter([9,8],[3,4],s=[75,90],color=['#17658a','#743c85'],zorder=5)
ax.annotate('S = 6',(3,9),xytext=(5,7),textcoords='offset points',fontsize=10,color='#566168')
ax.annotate('S = 6',(9,3),xytext=(4,-18),textcoords='offset points',fontsize=10,color='#17658a')
ax.text(8.13,8.85,'S can\nsecure 8',fontsize=11,color='#285d38',ha='left')
ax.set_xlim(0,10);ax.set_ylim(1,10)
ax.set_xticks(range(0,11));ax.set_yticks(range(1,11))
ax.set_xlabel("S's payoff after N best responds",fontsize=11)
ax.set_ylabel("C's payoff",fontsize=11)
ax.set_title('Nine buildings: C opens at site 4',fontsize=13,pad=12)
ax.grid(alpha=.17)
ax.legend(loc='lower left',fontsize=9,framealpha=.96)
fig.tight_layout()
fig.savefig('computational-game-theory-location-continuations.png',facecolor='white',transparent=False)
