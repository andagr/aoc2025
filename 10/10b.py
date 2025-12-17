from dataclasses import dataclass
import re
from itertools import product
from collections import defaultdict
import numpy as np


@dataclass
class Machine:
    junctions: np.array[int]
    buttons: np.array[list[int]]

    @staticmethod
    def parse(line: str):
        junctions = [int(si) for si in re.search(r"\{(.+)\}", line).group(1).split(",")]
        button_positions = [
            [int(i) for i in re.findall(r"\d+", b)]
            for b in re.findall(r"\(.+?\)+", line)
        ]
        buttons = []
        for bps in button_positions:
            button = [0] * len(junctions)
            for bp in bps:
                button[bp] = 1
            buttons.append(button)
        return Machine(np.array(junctions), np.array(buttons))

def build_parity_dict(buttons):
    parity_dict = defaultdict(list)
    value_dict = {}
    
    for button_mask in product((0, 1), repeat=len(buttons)):
        junction_changes = np.zeros(len(buttons[0]), dtype=int)
        for i, pressed in enumerate(button_mask):
            if pressed:
                junction_changes += buttons[i]
        
        parity = tuple(junction_changes % 2)
        parity_dict[parity].append(button_mask)
        value_dict[button_mask] = junction_changes
    
    return parity_dict, value_dict

def solve2(junctions, parity_dict, value_dict):
    if np.all(junctions == 0):
        return 0
    
    if np.any(junctions < 0):
        return 1000000
    
    result = 1000000
    current_parity = tuple(junctions % 2)
    
    for button_mask in parity_dict.get(current_parity, []):
        joltage_drops = value_dict[button_mask]
        next_junctions = (junctions - joltage_drops) // 2
        next_result = solve2(next_junctions, parity_dict, value_dict)
        result = min(result, np.sum(button_mask) + 2 * next_result)
    
    return result

machines = [Machine.parse(line) for line in open("input.txt", mode="r")]

total = 0
i = 1
for m in machines:
    parity_dict, value_dict = build_parity_dict(m.buttons)
    curr = solve2(m.junctions, parity_dict, value_dict)
    print(i, curr)
    total += curr
    i += 1
print(total)
