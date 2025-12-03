
def is_repeating(number_input: int) -> bool:
    # Turn the number into text so we can work with digits easily
    num_str = str(number_input)
    number_len = len(num_str)

    # Try pattern lengths from 1 digit up to half the length of the number
    # (a pattern must appear at least twice, so it can't be longer than half the number's length)
    for pattern_len in range(1, number_len // 2 + 1):
        # If the number length is not a multiple of the pattern length,
        # then this pattern length cannot be a repeating pattern
        if number_len % pattern_len != 0:
            continue

        # Extracts the first possible pattern length from the num_str
        pattern = num_str[:pattern_len]

        # Works out how many times pattern_len fits into num_len
        repeat_times = number_len // pattern_len

        # Repeat the pattern for the number of times it fits
        # and see if it rebuilds the original number
        if pattern * repeat_times == num_str:
            return True

    # If no pattern worked, then this number is not made of a repeating pattern
    return False


with open('day_2/puzzle_input.txt', 'r') as puzzle_input:
    ranges = puzzle_input.read().strip().split(',')
    answer = 0

    for id_range in ranges:
        start, end = map(int, id_range.split('-'))
        # check each number between the start and end
        for number in range(start, end + 1):
            # if number has a repeating pattern - add it to the answer
            if is_repeating(number):
                answer += number

    print(answer)
