

with open('day_2/puzzle_input.txt', 'r') as puzzle_input:
    ranges = puzzle_input.read().strip().split(',')
    answer = 0
    for id_range in ranges:
        start, end = map(int, id_range.split('-'))
        for number in range(start, end + 1):
            num_str = str(number)
            if len(num_str) % 2 != 0:
                continue

            mid = len(num_str) // 2
            first_half = str(int(num_str[:mid]))
            second_half = str(int(num_str[mid:]))
            if first_half == second_half:
                answer += number
    print(answer)


        # for each number in the range
        # split it in half - see if one half matches the other
        # check for leading zeros
