"""Plot exact settled RC responses. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white'})
A, tau = 10.0, 0.05

def response(t, frequency):
    half_period = 0.5/frequency
    local = np.remainder(t, 1/frequency)
    peak = A*np.tanh(1/(4*frequency*tau))
    return np.where(local < half_period,
                    A-(A+peak)*np.exp(-local/tau),
                    -A+(A+peak)*np.exp(-(local-half_period)/tau))

fig, axes = plt.subplots(3, 1, figsize=(10, 8.2), layout='constrained')
cycles = np.linspace(0, 2, 20001)
for ax, frequency, label in zip(axes, (1000, 10, 0.1), ('1 kHz', '10 Hz', '0.1 Hz')):
    time = cycles/frequency
    output = response(time, frequency)
    if frequency != 1000:
        input_voltage = np.where(np.remainder(cycles, 1) < 0.5, A, -A)
        ax.plot(cycles, input_voltage, color='#888888', linestyle='--', linewidth=1.1, label='input')
    ax.plot(cycles, output, color='#1f5f99', linewidth=2.3, label='capacitor')
    peak = A*np.tanh(1/(4*frequency*tau))
    ax.set_title(f'{label}: settled extrema ±{peak:.4g} V', loc='left')
    ax.set_ylabel('Voltage (V)')
    ax.set_xlabel('Time / input period')
    ax.set_xlim(0, 2)
    ax.grid(alpha=0.22)
    ax.axhline(0, color='black', linewidth=0.6)
    ax.set_ylim((-0.065, 0.065) if frequency == 1000 else (-11.5, 11.5))
    if frequency == 10:
        ax.legend(loc='upper right', ncols=2, fontsize=10)
    if frequency == 0.1:
        inset = ax.inset_axes([0.64, 0.28, 0.30, 0.43])
        edge_t = np.linspace(0, 0.25, 500)
        inset.plot(edge_t, response(edge_t, frequency), color='#1f5f99', linewidth=1.8)
        inset.set_title('One rising edge', fontsize=9)
        inset.set_xlabel('Time (s)', fontsize=9)
        inset.tick_params(labelsize=8)
        inset.set_ylim(-11, 11)
        inset.grid(alpha=0.2)
fig.suptitle('RC low-pass response: R = 10 kΩ, C = 5 μF, input ±10 V', fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
