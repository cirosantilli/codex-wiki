"""Original Fibonacci plots; saves a basename PNG to the cwd."""
from pathlib import Path
from math import sqrt
import matplotlib.pyplot as plt

def binet(n):
    phi=(1+sqrt(5))/2;psi=(1-sqrt(5))/2
    return round((phi**n-psi**n)/sqrt(5))

# Independent integer recurrence verifies the range used by the answer code.
a,b=0,1
for n in range(51):
    assert binet(n)==a
    a,b=b,a+b
list50=[binet(n) for n in range(1,51)]
fig,axes=plt.subplots(2,2,figsize=(8,6),layout='constrained',facecolor='white')
for ax,stop in zip(axes.flat,[10,20,30,40]):
    ax.plot(range(1,stop+1),list50[:stop],color='#245c9f',linewidth=2)
    ax.set(title=f'n = {stop}',xlabel='n',ylabel='f(n)')
    ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-2-fibonacci.png'),dpi=125,facecolor='white')
plt.close(fig)
