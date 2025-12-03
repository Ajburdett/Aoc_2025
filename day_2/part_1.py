
with open('day_2/puzzle_input.txt', 'r') as puzzle_input:
    ranges = puzzle_input.read().strip().split(',')
    answer = 0

    for id_range in ranges:
        # Split "start-end" into two parts, convert both to integers
        start, end = map(int, id_range.split('-'))

        # Loop through every integer from start up to and including end
        for number in range(start, end + 1):
            # Convert the current number to a string, so we can work with its digits
            num_str = str(number)

            # If the length of the number of digits is odd, skip it immediately
            if len(num_str) % 2 != 0:
                continue

            # Find the midpoint of the number
            mid = len(num_str) // 2

            # Take the first half of the digits,
            # convert to int, then back to str (to strip leading zeros)
            first_half = str(int(num_str[:mid]))

            # Take the second half of the digits, also convert to int and back to str
            # to strip any leading zeros in that half as well
            second_half = str(int(num_str[mid:]))

            if first_half == second_half:
                answer += number

    print(answer)

        # for each number in the range
        # split it in half - see if one half matches the other
        # check for leading zeros
