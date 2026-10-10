"""Original fixed-reservoir energy model, not a fit to biological measurements.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
All energies are molar; chosen n=10 and three ATP per turn. No leaks/slip.
The extra transport debit is hypothetical and does not change motor balance.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


F = 96485.0
N = 10
ATP_PER_TURN = 3
G_ATP = 50.0  # kJ / mol ATP; fixed local synthesis cost, not standard-state value
PMF = .180  # V; positive downhill magnitude
EXTRA_EQUIVALENTS = 1.0  # chosen combined transport cost per delivered ATP
balance = ATP_PER_TURN * G_ATP * 1000 / (N * F)
motor_input = N / ATP_PER_TURN * F * PMF / 1000
transport_input = EXTRA_EQUIVALENTS * F * PMF / 1000
assert np.isclose(motor_input, 57.891)
assert np.isclose(transport_input, 17.3673)
assert .155 < balance < .156

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (ax, budget) = plt.subplots(1, 2, figsize=(11, 5.9), gridspec_kw={"width_ratios": [1.15, 1]})
fig.patch.set_facecolor("white")
fig.suptitle("A chosen ATP synthase energy budget", fontsize=19, y=.96)
fig.text(.5, .88, "n = 10 • 3 ATP / turn • gATP = 50 kJ/mol • fixed reservoirs • tight coupling • no leak",
         ha="center", fontsize=11)
fig.subplots_adjust(top=.76, bottom=.23, left=.09, right=.97, wspace=.4)
p = np.linspace(.1, .22, 300)
dg = ATP_PER_TURN * G_ATP - N * F * p / 1000
ax.axhspan(0, 60, color="#f9e4d4", alpha=.8)
ax.axhspan(-70, 0, color="#dfefdf", alpha=.8)
ax.axhline(0, color="#54636b", lw=1)
ax.plot(p*1000, dg, color="#176b9a", lw=2.6)
ax.plot(balance*1000, 0, "o", color="#172c3c")
ax.annotate("Balance: 155.46 mV\n(no net driving margin)", xy=(balance*1000, 0),
            xytext=(107, -45), fontsize=10, arrowprops={"arrowstyle": "->", "color": "#172c3c"})
for voltage, offset in [(.14, (-65, 20)), (.18, (9, -22))]:
    val = ATP_PER_TURN*G_ATP - N*F*voltage/1000
    ax.plot(voltage*1000, val, "o", color="#176b9a")
    ax.annotate(f"{voltage*1000:.0f} mV\n{val:+.3f}", (voltage*1000, val),
                xytext=offset, textcoords="offset points", fontsize=10)
ax.text(216, 46, "Reverse favoured", ha="right", color="#9a4a1a")
ax.text(216, -60, "Synthesis favoured", ha="right", color="#28754e")
ax.set(xlim=(100, 220), ylim=(-67, 57), xlabel=r"Downhill driving magnitude $\Delta p_{\rm drive}$ (mV)",
       ylabel="ΔG per mole of complete turns (kJ/mol)")
ax.set_title(r"Motor balance: $150-10F\Delta p_{\rm drive}/1000$", fontsize=12, pad=13)

# Distinct system boundary: the stacked bars describe expenditure, not ΔGturn.
budget.bar([0, 1], [motor_input, motor_input], width=.58, color="#9ac5da", ec="white")
budget.bar(1, transport_input, bottom=motor_input, width=.58, color="#eab47e", ec="white")
budget.axhline(G_ATP, color="#28754e", lw=2, linestyle="--")
budget.text(.5, 46, "50 stored in ATP", color="#28754e", ha="center", fontsize=11,
            bbox={"fc": "white", "ec": "none", "pad": 1.5})
budget.text(0, motor_input+2, f"{motor_input:.3f}", ha="center", weight="bold")
budget.text(1, motor_input+transport_input+2, f"{motor_input+transport_input:.3f}", ha="center", weight="bold")
budget.text(1, motor_input+transport_input/2, "+1 H⁺ equivalent\n17.367", ha="center", va="center", fontsize=10)
budget.text(0, 24, "10/3 H⁺\nthrough motor", ha="center", fontsize=10)
budget.text(1, 24, "10/3 H⁺\nthrough motor", ha="center", fontsize=10)
budget.set(xticks=[0, 1], xticklabels=["Motor only\n86.4% stored/input", "With transport debit\n66.4% stored/input"],
           ylim=(0, 88), xlim=(-.65, 1.65), ylabel="Gradient expenditure per ATP (kJ/mol)")
budget.set_title("Expenditure at 180 mV", fontsize=12, pad=13)
budget.tick_params(axis="x", labelsize=10)
for a in (ax, budget):
    a.spines[["top", "right"]].set_visible(False)
fig.text(.5, .085, "Transport debit is an explicit hypothetical cost per delivered ATP, not extra H⁺ through F₀.\n"
         "It changes system expenditure; the motor balance point above is unchanged. No rate law is assumed.",
         ha="center", va="center", fontsize=10)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
plt.close(fig)
