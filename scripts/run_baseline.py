from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime

from mcrmss.config import SimulationConfig
from mcrmss.simulation import run_simulation


def _make_output_dir(base: str = "data/outputs") -> Path:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(base) / f"baseline_{ts}"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run baseline Monte Carlo mission reliability & sustainment simulation."
    )
    parser.add_argument("--days", type=int, default=180, help="Simulation horizon in days.")
    parser.add_argument("--trials", type=int, default=200, help="Number of Monte Carlo trials.")
    parser.add_argument("--seed", type=int, default=42, help="Base RNG seed.")
    parser.add_argument(
        "--out",
        type=str,
        default="data/outputs",
        help="Base output directory (timestamped subdir will be created).",
    )
    args = parser.parse_args()

    cfg = SimulationConfig(
        horizon_days=args.days,
        trials=args.trials,
        seed=args.seed,
    )

    results = run_simulation(cfg)

    out_dir = _make_output_dir(args.out)
    (out_dir / "summary.json").write_text(json.dumps(results["summary"], indent=2))
    (out_dir / "config.json").write_text(json.dumps(results["config"], indent=2))

    # NOTE: Raw trials can be large; write only if you need it.
    # Uncomment to dump raw per-day per-trial metrics.
    # (out_dir / "raw_trials.json").write_text(
    #     json.dumps(results["trials"], default=lambda o: o.__dict__, indent=2)
    # )

    print("✅ Baseline run complete")
    print(f"- Output folder: {out_dir}")
    print(f"- Mean mission success rate: {results['summary']['mean_success_rate']:.4f}")
    print(f"- Mean availability: {results['summary']['mean_availability']:.4f}")


if __name__ == "__main__":
    main()