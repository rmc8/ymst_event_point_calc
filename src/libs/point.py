from decimal import Decimal, getcontext


class YmstEventPointCalculator:
    def __init__(
        self,
        score: int,
        stamina_consumption: int,
        event_bonus: float,
        basic_reward: float,
    ) -> None:
        self.score = Decimal(score)
        self.stamina_consumption = Decimal(stamina_consumption)
        self.event_bonus = Decimal(event_bonus)
        self.basic_reward = Decimal(basic_reward)

    def score_adjustment(self) -> Decimal:
        getcontext().prec = 10
        adjustment_multiplier = Decimal(1.0)
        # 300万までの処理
        if self.score <= 3_000_000:
            adjustment_multiplier += (self.score / 600_000) * Decimal(0.1)
        # 300万から1500万までの処理
        elif self.score <= 15_000_000:
            adjustment_multiplier += Decimal(0.5)
            adjustment_multiplier += ((self.score - 3_000_000) / 6_000_000) * Decimal(
                0.1
            )
        # 1500万以降の処理
        else:
            adjustment_multiplier += Decimal(0.5 + 0.2)
            adjustment_multiplier += ((self.score - 15_000_000) / 1_000_000) * Decimal(
                0.01
            )
        return adjustment_multiplier

    def calc(self) -> int:
        event_point = (
            self.stamina_consumption
            * self.score_adjustment()
            * (1 + self.event_bonus)
            * self.basic_reward
            * 100
        )
        return int(event_point)
