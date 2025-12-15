from dataclasses import dataclass
import re
from itertools import combinations, groupby
from functools import reduce
import operator


@dataclass
class Machine:
    light: int
    buttons: list[int]

    @staticmethod
    def parse(line: str):
        light_list = list(re.search(r"\[([.#]+)\]", line).group(1))
        light_list.reverse()
        light = int("".join(light_list).replace(".", "0").replace("#", "1"), 2)
        button_positions = [
            [int(i) for i in re.findall(r"\d+", b)]
            for b in re.findall(r"\(.+?\)+", line)
        ]
        buttons = [sum(1 << pos for pos in positions) for positions in button_positions]
        return Machine(light, buttons)


def sorted_combinations(l):
    return [list(combo) for i in range(1, len(l) + 1) for combo in combinations(l, i)]


machines = [Machine.parse(line) for line in open("input.txt", mode="r")]
print(
    sum(
        [
            len(
                [
                    b
                    for b in sorted_combinations(m.buttons)
                    if reduce(operator.xor, b) == m.light
                ][0]
            )
            for m in machines
        ]
    )
)
