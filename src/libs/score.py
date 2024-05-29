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
