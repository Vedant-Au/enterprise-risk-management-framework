from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis import prepare_fmea, prepare_risk_register, risk_zone


class EnterpriseRiskTests(unittest.TestCase):
    def test_zone_thresholds(self) -> None:
        self.assertEqual(risk_zone(6), "Green")
        self.assertEqual(risk_zone(7), "Amber")
        self.assertEqual(risk_zone(14), "Amber")
        self.assertEqual(risk_zone(15), "Red")

    def test_register_scores_reconcile(self) -> None:
        frame = pd.read_csv(ROOT / "data/reference/risk_register.csv")
        result = prepare_risk_register(frame)
        self.assertTrue((result["inherent_score"] == result["likelihood"] * result["impact"]).all())
        self.assertTrue((result["residual_score"] <= result["inherent_score"]).all())

    def test_fmea_rpn_matches_report_examples(self) -> None:
        frame = prepare_fmea(pd.read_csv(ROOT / "data/reference/fmea.csv"))
        values = dict(zip(frame["failure_mode"], frame["rpn"], strict=True))
        self.assertEqual(values["Hose assembly defect not detected"], 168)
        self.assertEqual(values["Pressure test miscalibration"], 108)

    def test_duplicate_ids_are_rejected(self) -> None:
        frame = pd.read_csv(ROOT / "data/reference/risk_register.csv")
        frame.loc[1, "risk_id"] = frame.loc[0, "risk_id"]
        with self.assertRaisesRegex(ValueError, "unique"):
            prepare_risk_register(frame)


if __name__ == "__main__":
    unittest.main()
