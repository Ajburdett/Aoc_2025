# python
output_joltage = 0
batteries_on = 12  # number of batteries to turn on per bank

def find_best_joltage(bank: str, number_of_batteries: int = batteries_on) -> int:
    """
    Pick exactly `number_of_batteries` digits from `bank` (in order) to form
    the largest possible integer. Uses a greedy O(n * k) algorithm.
    """
    digits = [int(c) for c in bank.strip()]
    n = len(digits)
    k = number_of_batteries

    result = []
    start = 0
    remaining = k

    while remaining > 0:
        # last index we can start from and still have enough digits left
        end = n - remaining
        # pick the max digit in this window
        max_pos = max(range(start, end + 1), key=digits.__getitem__)
        result.append(digits[max_pos])
        start = max_pos + 1
        remaining -= 1

    value = 0
    for d in result:
        value = value * 10 + d
    return value


with open('day_3/input.txt', 'r') as puzzle_input:
    for battery_bank in puzzle_input:
        output_joltage += find_best_joltage(battery_bank)

print(output_joltage)
