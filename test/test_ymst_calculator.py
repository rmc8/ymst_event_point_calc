import sys
import os
import pytest
from typing import List, Tuple

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from libs.point import YmstEventPointCalculator  # noqa: E402


def test_score_adjustment() -> None:
    test_cases: List[Tuple[int, float]] = [
        (1500000, 1.25),
        (3000000, 1.50),
        (4500000, 1.525),
        (6000000, 1.55),
        (7500000, 1.575),
        (15000000, 1.70),
        (16000000, 1.71),
        (17500000, 1.725),
        (19000000, 1.74),
        (20000000, 1.75),
    ]

    for score, expected in test_cases:
        calculator = YmstEventPointCalculator(score, 0, 0.0, 0)
        result = calculator.score_adjustment()
        assert float(result) == pytest.approx(
            expected, rel=1e-9
        ), f"Failed for score: {score}, expected: {expected}, got: {result}"


if __name__ == "__main__":
    pytest.main()
