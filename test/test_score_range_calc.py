import os
import sys
import pytest
from typing import Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from libs.score import ScoreCalculator

TOLERANCE = 2


@pytest.mark.parametrize(
    "event_point, lower_score, upper_score",
    [
        (100, None, None),
        (120, 0, 49999),
        (138, 900000, 949999),
        (164, 2200000, 2249999),
        (181, 3500000, 3999999),
        (202, 14000000, 14499999),
        (205, 15833334, 16666666),
        (269, 69166667, 69999999),
        (348, 135000000, 135833333),
    ],
)
def test_score_calculator(
    event_point: int, lower_score: Optional[int], upper_score: Optional[int]
) -> None:
    calculator = ScoreCalculator(
        event_point=event_point,
        stamina_consumption=1,
        event_bonus=0.0,
        basic_reward=1.2,
    )

    lower_limit = calculator.calc_score_lower_limit()
    upper_limit = calculator.calc_score_upper_limit()

    if lower_score is None:
        assert lower_limit is None
    else:
        assert lower_limit == pytest.approx(lower_score, abs=TOLERANCE)

    if upper_score is None:
        assert upper_limit is None
    else:
        assert upper_limit == pytest.approx(upper_score, abs=TOLERANCE)


if __name__ == "__main__":
    pytest.main()
