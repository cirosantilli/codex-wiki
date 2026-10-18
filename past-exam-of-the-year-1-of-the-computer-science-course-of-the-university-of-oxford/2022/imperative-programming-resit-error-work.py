"""Original ideal-precision work comparison. Python 3.14.4, Matplotlib 3.10.7.

Reference errors use Decimal at 80 digits. Counts are for the solution's exact
loop structures, counting each multiplication and division once, not bit cost.
The image is written to the current working directory.
"""
from decimal import Decimal, localcontext
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def accuracy_work():
    with localcontext() as context:
        context.prec = 80
        e = Decimal(1).exp()
        def ea(n):
            a = Decimal(n)
            return (1 + 1/a) ** n
        def ec(n):
            a = Decimal(n)
            return (a+1)*(1+1/a)**n-a*(1+1/(a-1))**(n-1)
        def threshold(f, start, tolerance):
            if abs(f(start)-e) <= tolerance:
                return start
            low, high = start, 2*start
            while abs(f(high)-e) > tolerance:
                low, high = high, 2*high
            while high-low > 1:
                middle = low+(high-low)//2
                if abs(f(middle)-e) <= tolerance:
                    high = middle
                else:
                    low = middle
            return high
        rows = []
        for digits in range(1, 9):
            tolerance = Decimal(5)*Decimal(10)**(-digits-1)
            na = threshold(ea, 1, tolerance)
            nc = threshold(ec, 2, tolerance)
            nb, term, total = 0, Decimal(1), Decimal(1)
            while abs(total-e) > tolerance:
                nb += 1
                term /= nb
                total += term
            assert na <= 2**31-1
            assert abs(ea(na)-e) <= tolerance
            assert na == 1 or abs(ea(na-1)-e) > tolerance
            assert abs(ec(nc)-e) <= tolerance
            assert nc == 2 or abs(ec(nc-1)-e) > tolerance
            rows.append({"digits":digits,"ea_n":na,"eb_n":nb,"ec_n":nc,
                         "ea_work":na.bit_length()+na.bit_count()+1,
                         "eb_work":nb,
                         "ec_work":2*(nc-1).bit_length()+2*(nc-1).bit_count()+5,
                         "ea_reference_error":str(abs(ea(na)-e)),
                         "eb_reference_error":str(abs(total-e)),
                         "ec_reference_error":str(abs(ec(nc)-e))})
        return rows

def main():
    rows = accuracy_work()
    fig, ax = plt.subplots(figsize=(8.3, 4.5), layout="constrained")
    styles = [("ea_work","Fast binomial power","#276792","o"),
              ("ec_work","Parallel powers and subtraction","#a5483c","s"),
              ("eb_work","Reciprocal-factorial sum","#2e874b","^")]
    for key, label, color, marker in styles:
        ax.plot([r["digits"] for r in rows],[r[key] for r in rows],
                color=color,marker=marker,label=label)
    ax.set(xlabel="Requested decimal places d (absolute error ≤ 0.5 × 10⁻ᵈ)",
           ylabel="Multiplications + divisions",
           title="1(d): arithmetic work with high-precision reference errors",
           xticks=list(range(1,9)),ylim=(0,65))
    ax.grid(axis="y",color=".88",lw=.7)
    ax.legend(loc="upper left",fontsize=9)
    ax.text(.98,.04,"Ideal-precision comparison; Double rounding can alter accuracy",
            transform=ax.transAxes,ha="right",fontsize=8)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,
                facecolor="white",transparent=False)
    print(json.dumps(rows))

if __name__ == "__main__":
    main()
