from typing import List, Dict
from libs.point import YmstEventPointCalculator as PointCalc


BASIC_REWARD: List[float] = [(r / 100) for r in range(115, 215, 5)]
EVENT_BONUS: List[float] = [(p / 100) for p in range(0, 275, 25)]
STAMINA_CONSUMPTION: Dict[int, int] = {
    0: 1,
    1: 5,
    2: 10,
    3: 14,
    4: 18,
    5: 21,
    6: 24,
    7: 26,
    8: 28,
    9: 29,
    10: 30,
}


def main() -> None:
    pc = PointCalc(
        score=6000000,
        stamina_consumption=1,
        event_bonus=0.0,
        basic_reward=1.2,
    )
    point = pc.calc()
    ad = pc.score_adjustment()
    print(point)
    print(ad)


if __name__ == "__main__":
    main()
