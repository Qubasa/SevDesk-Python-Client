from typing import Union

import cattrs


class Unset:
    def __bool__(self) -> bool:
        return False


UNSET: Unset = Unset()

cattrs.register_structure_hook(
    Union[Unset, str], lambda value, _: UNSET if value is None else value
)

Unit = {
    "Stk": 1,
    "m2": 2,
    "m": 3,
    "kg": 4,
    "t": 5,
    "lfm": 6,
    "pauschal": 7,
    "m3": 8,
    "Std": 9,
    "km": 10,
    "%": 11,
    "Tag(e)": 12,
    "L": 13,
}
