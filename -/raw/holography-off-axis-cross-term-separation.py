"""Original periodic off-axis hologram; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

Run from _media. Uses NumPy FFT only, with no propagation or SciPy. Checks
analytic Fourier coefficients, complex-field recovery and playback orders.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

N = 1024
x = np.arange(N) / N
O = .2*np.exp(2j*np.pi*3*x) + .1*np.exp(-2j*np.pi*5*x)
R = np.exp(2j*np.pi*20*x)
I = np.abs(R + O)**2
analytic = 1.05 + .04*np.cos(2*np.pi*8*x) + .4*np.cos(2*np.pi*17*x) + .2*np.cos(2*np.pi*25*x)
np.testing.assert_allclose(I, analytic, atol=2e-14, rtol=0)
coeff = np.fft.fft(I)/N
freq = np.fft.fftfreq(N, 1/N)
expected = np.zeros(N, dtype=complex)
for m, a in [(0,1.05), (8,.02),(-8,.02),(17,.2),(-17,.2),(25,.1),(-25,.1)]:
    expected[m % N] = a
np.testing.assert_allclose(coeff, expected, atol=2e-14, rtol=0)
mask = (freq >= -30) & (freq <= -12)
recovered = R*np.fft.ifft(N*coeff*mask)
np.testing.assert_allclose(recovered, O, atol=2e-14, rtol=0)
t0, beta = .3, .01
t = t0 + beta*I
playback = R*t
background = (t0+beta*(1+np.abs(O)**2))*R
desired = beta*O
conjugate = beta*R**2*O.conj()
np.testing.assert_allclose(playback, background+desired+conjugate, atol=2e-14, rtol=0)
assert t.min() >= .3049-1e-14 and t.max() <= .3169+1e-14
for term, modes in [(desired,{3:.002,-5:.001}), (conjugate,{37:.002,45:.001}), (background,{20:.3105,12:.0002,28:.0002})]:
    target = np.zeros(N, dtype=complex)
    for m,a in modes.items(): target[m % N] = a
    np.testing.assert_allclose(np.fft.fft(term)/N, target, atol=2e-14, rtol=0)
error = float(np.max(np.abs(recovered-O)))
print(f'Max complex recovery error: {error:.3g}; all analytic and playback checks passed')

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(2, 2, figsize=(10, 6.2))
fig.subplots_adjust(left=.08, right=.975, top=.86, bottom=.1, hspace=.49, wspace=.28)
fig.suptitle('A tilted reference separates the two encoded fields', fontsize=16)
ax=axes[0,0]
ax.plot(x,I,color='#333333',lw=1.3)
ax.set(title=r'Record $I=|R+O|^2$', xlabel='x (unit interval)',ylabel='Intensity (chosen units)',xlim=(0,1))
ax=axes[0,1]
colors={0:'.35',8:'.35',-8:'.35',-17:'#1967a3',-25:'#1967a3',17:'#ba5316',25:'#ba5316'}
for m in sorted(colors):
    a=abs(coeff[m%N]); ax.vlines(m,0,a,color=colors[m],lw=2);ax.plot(m,a,'o',color=colors[m],ms=4)
ax.axvspan(-30,-12,color='#1967a3',alpha=.12,label='Retained band')
ax.set(title='Normalized FFT coefficients',xlabel='Spatial frequency (cycles / unit)',ylabel='Coefficient magnitude',xlim=(-33,33),ylim=(0,1.2))
ax.text(0,1.09,'Background',ha='center',fontsize=9)
ax.text(-21,.36,r'$R^*O$',ha='center',color='#1967a3')
ax.text(21,.36,r'$RO^*$',ha='center',color='#ba5316')
ax.legend(loc='upper left',fontsize=8)
for ax, part, label in [(axes[1,0],np.real,'Real'),(axes[1,1],np.imag,'Imaginary')]:
    ax.plot(x,part(O),color='#1967a3',lw=2,label='Chosen O')
    ax.plot(x[::16],part(recovered[::16]),'o',ms=3,mfc='white',mec='#ba5316',label='Recovered')
    ax.set(title=f'Recovered {label.lower()} part of O',xlabel='x (unit interval)',ylabel='Complex amplitude',xlim=(0,1),ylim=(-.34,.34))
    ax.legend(fontsize=8,loc='upper right')
for ax in axes.flat:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.16)
fig.text(.5,.015, 'Chosen periodic field; N = 1024. Exact integer bins avoid spectral leakage. No measured data.',ha='center',fontsize=10,color='.35')
fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png',dpi=120,facecolor='white')
plt.close(fig)
