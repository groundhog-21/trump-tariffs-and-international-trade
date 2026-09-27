"""Reproduce the three blog figures from the prepared Census snapshot.

Chart contract: Q1 uses two period-mean bars; Q2 uses a coefficient and
95% interval; Q3 uses two signed balance bars. All use the same 403
monthly observations, blue marks, direct labels, and explicit units.
Export static PNG files for the Markdown blog and Medium upload.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "figures"
BLUE = "#2563A6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "text.parse_math": False})
data = pd.read_csv(ROOT / "data/processed/analysis_data.csv")
data["time"] = np.arange(len(data))
assert len(data) == 403
labels = ["Jan 1993–Dec 2024\n384 months", "Jan 2025–Jul 2026\n19 months"]


def canvas(title, subtitle):
    """Create a consistent figure with room for labels and source notes."""
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(left=0.13, right=0.95, bottom=0.32, top=0.76)
    fig.text(0.13, 0.93, title, fontsize=19, weight="bold")
    fig.text(0.13, 0.86, subtitle, fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#E5E7EB")
    fig.text(0.13, 0.045, "Source: included US Census Bureau snapshot; author's calculations.", fontsize=10)
    return fig, ax


def save(fig, name):
    """Save a publication image and close its figure."""
    fig.savefig(OUT / name, dpi=180, facecolor="white")
    plt.close(fig)


growth = data.groupby("trump_second_term")["imports_yoy_pct"].mean()
fig, ax = canvas("Q1 · Average year-over-year import growth", "Monthly growth rates averaged within each period | January 1993–July 2026")
ax.bar(labels, growth, color=BLUE, width=0.5)
ax.set(ylabel="Average year-over-year growth (%)", ylim=(0, 8))
for i, value in enumerate(growth):
    ax.text(i, value + 0.2, f"{value:.2f}%", ha="center", weight="bold")
fig.text(0.13, 0.12, "Difference: −2.37 percentage points; insufficient evidence of lower growth.\n95% interval for the difference: −10.29 to +5.55 points; one-sided p = 0.278.", fontsize=11)
save(fig, "q1-import-growth.png")

model = sm.OLS(data["imports"], sm.add_constant(data[["time", "trump_second_term"]])).fit(cov_type="HAC", cov_kwds={"maxlags": 12, "use_correction": True}, use_t=True)
estimate = model.params["trump_second_term"] / 1000
low, high = model.conf_int().loc["trump_second_term"] / 1000
fig, ax = canvas("Q2 · Import difference relative to a linear trend", "Second-term coefficient | 403 monthly observations | Nominal US$ billions per month")
ax.errorbar(estimate, 0, xerr=[[estimate-low], [high-estimate]], fmt="o", color=BLUE, capsize=9, markersize=10, linewidth=3)
ax.axvline(0, color="#555555", linestyle="--")
ax.set(xlim=(-10, 50), ylim=(-1, 1), yticks=[], xlabel="Difference from fitted linear trend (US$ billions per month)")
ax.text(estimate, 0.35, f"+${estimate:.2f}bn", ha="center", weight="bold", fontsize=16)
ax.text(estimate, -0.4, f"95% confidence interval: +${low:.2f}bn to +${high:.2f}bn", ha="center")
fig.text(0.13, 0.12, "The estimate is above zero, offering no support for imports below this trend.\nOLS with HAC uncertainty (12 lags); an association, not a causal tariff effect.", fontsize=11)
save(fig, "q2-import-levels.png")

balance = data.groupby("trump_second_term")["trade_balance"].mean()/1000
fig, ax = canvas("Q3 · Average monthly US goods trade balance", "Exports minus imports | January 1993–July 2026 | Negative values indicate deficits")
ax.bar(labels, balance, color=BLUE, width=0.5)
ax.axhline(0, color="#555555")
ax.set(ylabel="Average balance (nominal US$ billions)", ylim=(-125, 0))
for i, value in enumerate(balance):
    ax.text(i, value - 5, f"−${abs(value):.2f}bn", ha="center", va="top", weight="bold")
fig.text(0.13, 0.12, "Average deficit: $46.27bn larger per month during the second term.\nDescriptive comparison; unequal periods, no inflation or trend adjustment.", fontsize=11)
save(fig, "q3-trade-balance.png")
print(f"Generated three figures in {OUT}")
