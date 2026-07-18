from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent


def risk_zone(score: int) -> str:
    if not 1 <= score <= 25:
        raise ValueError("Risk score must be between 1 and 25.")
    if score <= 6:
        return "Green"
    if score <= 14:
        return "Amber"
    return "Red"


def prepare_risk_register(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"risk_id", "category", "risk_title", "owner", "likelihood", "impact", "residual_score"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if frame["risk_id"].duplicated().any():
        raise ValueError("risk_id must be unique.")
    if not frame[["likelihood", "impact"]].apply(lambda s: s.between(1, 5).all()).all():
        raise ValueError("Likelihood and impact must be between 1 and 5.")
    result = frame.copy()
    result["inherent_score"] = result["likelihood"] * result["impact"]
    if not result["residual_score"].between(1, 25).all():
        raise ValueError("Residual scores must be between 1 and 25.")
    if (result["residual_score"] > result["inherent_score"]).any():
        raise ValueError("Residual score cannot exceed inherent score in this model.")
    result["inherent_zone"] = result["inherent_score"].map(risk_zone)
    result["residual_zone"] = result["residual_score"].map(risk_zone)
    result["control_reduction"] = result["inherent_score"] - result["residual_score"]
    return result


def prepare_fmea(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"failure_mode", "severity", "occurrence", "detectability"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing FMEA columns: {sorted(missing)}")
    if not frame[["severity", "occurrence", "detectability"]].apply(lambda s: s.between(1, 10).all()).all():
        raise ValueError("FMEA inputs must be between 1 and 10.")
    result = frame.copy()
    result["rpn"] = result["severity"] * result["occurrence"] * result["detectability"]
    return result.sort_values("rpn", ascending=False)


def main() -> None:
    risks = prepare_risk_register(pd.read_csv(ROOT / "data/reference/risk_register.csv"))
    fmea = prepare_fmea(pd.read_csv(ROOT / "data/reference/fmea.csv"))
    tables = ROOT / "outputs/tables"
    figures = ROOT / "outputs/figures"
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    risks.to_csv(tables / "scored_risk_register.csv", index=False)
    fmea.to_csv(tables / "scored_fmea.csv", index=False)

    ordered = risks.sort_values("residual_score")
    colours = ordered["residual_zone"].map({"Green":"#4CAF50", "Amber":"#F2B134", "Red":"#D1495B"})
    fig, ax = plt.subplots(figsize=(9, 5.8))
    bars = ax.barh(ordered["risk_title"], ordered["residual_score"], color=colours)
    ax.bar_label(bars, padding=3)
    ax.set(title="Residual exposure remains concentrated in operational and cyber risks", xlabel="Residual risk score (1-25)", xlim=(0, 25))
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(figures / "residual_risk_priorities.png", dpi=180, facecolor="white")
    plt.close(fig)

    matrix = np.arange(1, 6)[:, None] * np.arange(1, 6)[None, :]
    fig, ax = plt.subplots(figsize=(7, 6))
    image = ax.imshow(matrix, origin="lower", cmap="RdYlGn_r", vmin=1, vmax=25)
    for row in range(5):
        for col in range(5):
            ax.text(col, row, str(matrix[row, col]), ha="center", va="center", weight="bold")
    ax.scatter(risks["impact"] - 1, risks["likelihood"] - 1, s=90, facecolors="none", edgecolors="#17324D", linewidths=2)
    ax.set_xticks(range(5), range(1, 6)); ax.set_yticks(range(5), range(1, 6))
    ax.set(xlabel="Impact", ylabel="Likelihood", title="Illustrative inherent-risk heat map")
    fig.colorbar(image, ax=ax, label="Likelihood x impact")
    fig.tight_layout()
    fig.savefig(figures / "risk_heatmap.png", dpi=180, facecolor="white")
    plt.close(fig)

    print(risks[["risk_id", "risk_title", "inherent_score", "residual_score", "residual_zone"]].to_string(index=False))


if __name__ == "__main__":
    main()
