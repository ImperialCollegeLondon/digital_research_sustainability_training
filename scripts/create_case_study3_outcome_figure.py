# /// script
# dependencies = [
#   "matplotlib",
# ]
# ///

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent


def create_case_study3_outcome_figure():
    # Sample data for the figure
    positions = np.array([0, 2])
    categories = ["DRAGONFLY", "LANCER"]
    pre_estimates = [51, 93]
    post_estimates = [38.25, 69.75]

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    trace = ax.bar(positions, pre_estimates, color="blue", label="Pre-Intervention")
    ax.bar_label(trace, padding=2)
    trace = ax.bar(
        positions + 0.8,
        post_estimates,
        color="orange",
        label="Post-Intervention",
    )
    ax.bar_label(trace, padding=2)

    # Add title and labels
    ax.set_title("Case Study 3 Outcomes")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Emissions (kg CO2e)")
    ax.legend()
    ax.set_xticks(positions + 0.4, categories)
    # Show the figure
    fig.tight_layout()
    fig.savefig(SCRIPT_DIR.parent / "episodes/fig/case_study3_outcomes.png")


if __name__ == "__main__":
    create_case_study3_outcome_figure()
