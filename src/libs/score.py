# import math
# from decimal import Decimal
# from typing import Optional


# class ScoreCalculator:
#     def __init__(
#         self,
#         event_point: int,
#         stamina_consumption: int,
#         event_bonus: float,
#         basic_reward: float,
#     ) -> None:
#         self.event_point = Decimal(event_point)
#         self.stamina_consumption = Decimal(stamina_consumption)
#         self.event_bonus = Decimal(event_bonus)
#         self.basic_reward = Decimal(basic_reward)

#     def get_score(self, score_adjustment: Decimal) -> int:
#         score = 0
#         if score_adjustment >= Decimal(1.7):
#             score += 15_000_000
#             f = float(score_adjustment - Decimal(1.7)) / 0.01
#             score += f * 1_000_000
#         elif score_adjustment >= Decimal(1.5):
#             score += 3_000_000
#             f = float(score_adjustment - Decimal(1.5)) / 0.1
#             score += f * 6_000_000
#         else:
#             f = float(score_adjustment - Decimal(1.0)) / 0.1
#             score += (f * 600_000)
#         print(score)
#         return math.ceil(score) - 1
#     def get_score_adjustment(self, _adjuster: int = 0) -> Decimal:
#         return (
#             (self.event_point + _adjuster)
#             / self.stamina_consumption
#             / (Decimal(1) + self.event_bonus)
#             / self.basic_reward
#             / Decimal(100)
#         )

#     def calc_score_lower_limit(self) -> Optional[int]:
#         score_adjustment = self.get_score_adjustment()
#         if score_adjustment < Decimal(1):
#             return None
#         return self.get_score(score_adjustment)

#     def calc_score_upper_limit(self) -> Optional[int]:
#         score_adjustment = self.get_score_adjustment(_adjuster=1)
#         if score_adjustment < Decimal(1):
#             return None
#         return self.get_score(score_adjustment) - 1


# # インスタンスの作成
# calculator = ScoreCalculator(
#     event_point=120, stamina_consumption=1, event_bonus=0.0, basic_reward=1.2
# )

# # スコアの下限を計算
# score_lower_limit = calculator.calc_score_lower_limit()
# print(score_lower_limit)

import math
from decimal import Decimal
from typing import Optional


class ScoreCalculator:
    def __init__(
        self,
        event_point: int,
        stamina_consumption: int,
        event_bonus: float,
        basic_reward: float,
    ) -> None:
        self.event_point = Decimal(event_point)
        self.stamina_consumption = Decimal(stamina_consumption)
        self.event_bonus = Decimal(event_bonus)
        self.basic_reward = Decimal(basic_reward)

    def get_base_score_1(self, _adjuster: int = 0) -> Decimal:
        adjusted_ep = self.event_point + Decimal(_adjuster)
        return (adjusted_ep * Decimal("6e6")) / (
            (Decimal("100") * self.basic_reward)
            * (self.event_bonus * Decimal("100") + Decimal("100"))
            / (Decimal("100") * self.stamina_consumption)
        ) - Decimal("6e6")

    def get_base_score_2(self, _adjuster: int = 0) -> Decimal:
        adjusted_ep = self.event_point + Decimal(_adjuster)
        return (
            (adjusted_ep * Decimal("6e7"))
            / (
                (Decimal("100") * self.basic_reward)
                * (self.event_bonus * Decimal("100") + Decimal("100"))
                / (Decimal("100") * self.stamina_consumption)
            )
            - (Decimal("1.5") * Decimal("6e7"))
            + Decimal("3e6")
        )

    def get_base_score_3(self, _adjuster: int = 0) -> Decimal:
        adjusted_ep = self.event_point + Decimal(_adjuster)
        return (
            (adjusted_ep * Decimal("1e8"))
            / (
                (Decimal("100") * self.basic_reward)
                * (self.event_bonus * Decimal("100") + Decimal("100"))
                / (Decimal("100") * self.stamina_consumption)
            )
            - (Decimal("1.7") * Decimal("1e8"))
            + Decimal("15e6")
        )

    def get_score(self, is_upper: bool = False) -> Optional[int]:
        adjust = int(is_upper)
        if self.get_base_score_1(_adjuster=adjust) < 0:
            return
        elif self.get_base_score_1(_adjuster=adjust) < Decimal("3e6"):
            return int(self.get_base_score_1(_adjuster=adjust)) - adjust
        elif self.get_base_score_2(_adjuster=adjust) < Decimal("15e6"):
            return int(self.get_base_score_2(_adjuster=adjust)) - adjust
        return round(self.get_base_score_3(_adjuster=adjust)) - adjust

    def calc_score_lower_limit(self) -> Optional[int]:
        return self.get_score()

    def calc_score_upper_limit(self) -> Optional[int]:
        return self.get_score(is_upper=True)


# インスタンスの作成
calculator = ScoreCalculator(
    event_point=237, stamina_consumption=1, event_bonus=0.0, basic_reward=1.2
)

# スコアの下限を計算
score_lower_limit = calculator.calc_score_lower_limit()
score_upper_limit = calculator.calc_score_upper_limit()
print(score_lower_limit, score_upper_limit)
