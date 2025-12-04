
from itertools import combinations

output_joltage = 0

def find_best_joltage(bank: str):
    """
    Given a string like "12345", find the largest possible two‑digit number
    that can be made by turning on exactly two batteries, in their original order.
    For example, from "12345" we can get 12, 13, 14, 15, 23, 24, ... 45.
    45 is the highest joltage here for this battery bank
    """

    # Turn the input line into a list of individual digit integers.
    # `strip()` removes any newline at the end of the line.
    batteries = [int(x) for x in bank.strip()]

    # For every pair of positions (first, second) in the bank,
    # build the two‑digit number using the digit at `first` as the tens
    # and the digit at `second` as the ones.
    #
    # `combinations(range(len(batteries)), 2)` gives all index pairs (i, j)
    # where i < j, so we never reorder the digits and never pick the same one twice.
    #
    # Then return the maximum of all these possible two‑digit numbers.
    return max(
        batteries[first] * 10 + batteries[second]
        for first, second in combinations(range(len(batteries)), 2)
    )

with open('day_3/input.txt', 'r') as puzzle_input:
    for battery_bank in puzzle_input:
        output_joltage += find_best_joltage(battery_bank)

print(output_joltage)