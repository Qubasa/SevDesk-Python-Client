from typing import Union

import cattrs


class Unset:
    def __bool__(self) -> bool:
        return False


UNSET: Unset = Unset()

cattrs.register_structure_hook(
    Union[Unset, str], lambda value, _: UNSET if value is None else value
)
