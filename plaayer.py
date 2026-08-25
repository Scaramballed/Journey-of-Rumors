import shutil
from time import sleep
import functions  # ← ADD THIS IMPORT

def update_stat_animated(label, current_value, change, row):
    width = shutil.get_terminal_size().columns

    step = -1 if change < 0 else 1
    target = current_value + change

    while current_value != target:
        current_value += step

        print(
            f"\033[{row};{width - 25}H{label}: {current_value}%   ",
            end="",
            flush=True
        )

        sleep(0.02)

    return current_value


class Player:
    def __init__(self):
        self.health = 100
        self.craving = 95
        self.study_count = 0  # ← ADD THIS

    def pop_substance(self, craving_change):
        self.health = update_stat_animated(
            "HEALTH",
            self.health,
            -20,
            1
        )

        self.craving = update_stat_animated(
            "CRAVING",
            self.craving,
            craving_change,
            2
        )

        print("\033[4;1H", end="", flush=True)
        self._check_status()  # ← ADD THIS

    def change_health(self, amount):
        self.health = update_stat_animated(
            "HEALTH",
            self.health,
            amount,
            1
        )

        print("\033[4;1H", end="", flush=True)
        self._check_status()  # ← ADD THIS

    def change_craving(self, amount):
        self.craving = update_stat_animated(
            "CRAVING",
            self.craving,
            amount,
            2
        )
        print("\033[4;1H", end="", flush=True)
        self._check_status()  # ← ADD THIS

    def _check_status(self):  # ← ADD THIS ENTIRE METHOD
        """Internal method to check and trigger terminal states."""
        if self.health <= 0:
            functions.death()
        elif self.craving >= 100:
            functions.rehab()
        elif self.craving <= 0:
            functions.win()