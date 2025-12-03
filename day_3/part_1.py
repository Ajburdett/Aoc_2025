
from itertools import combinations
from unicodedata import digit

output_joltage = 0

def find_best_joltage(bank: str):

    batteries = [int(x) for x in bank.strip()]
    return max(
        batteries[i] * 10 + batteries[j]
        for i, j in combinations(range(len(batteries)), 2)
    )


with open('day_3/input.txt', 'r') as puzzle_input:
    for battery_bank in puzzle_input:
        output_joltage += find_best_joltage(battery_bank)

print(output_joltage)


    # Need to find the highest two number combination in each battery bank