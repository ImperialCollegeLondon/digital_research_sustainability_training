# /// script
# dependencies = [
#   "matplotlib",
# ]
# ///

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent


def create_case_study1_outcome_figure():
    # Sample data for the figure
    positions = np.array([0, 2, 4, 6])
    categories = ["Software Development", "GitHub Actions", "LLM Use", "Software Use"]
    pre_estimates = [0.496, 0.006, 0.001, 17]
    post_estimates = [0.496, 0.006, 0.001, 13.6]

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
    ax.set_title("Case Study 1 Outcomes")
    ax.set_xlabel("Activity")
    ax.set_ylabel("Emissions (kg CO2e)")
    ax.legend()
    ax.set_xticks(positions + 0.4, categories)
    # Show the figure
    fig.tight_layout()
    fig.savefig(SCRIPT_DIR.parent / "episodes/fig/case_study1_outcomes.png")


if __name__ == "__main__":
    create_case_study1_outcome_figure()
