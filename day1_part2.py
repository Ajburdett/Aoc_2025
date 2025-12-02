
current_position = 50
zero_count = 0

with open('input_day_1.txt', 'r') as puzzle_input:
    for rotation in puzzle_input:
        if rotation.startswith("L"):
            rotation_amount = int(rotation.strip("L"))

            # Count how many times we pass through 0 going left

            # If we are currently at position 0
            # the next time we hit 0 is after 100 clicks
            # (because 1 click left goes to 99,
            # then 99 more clicks are needed to get back to 0)

            # **Otherwise - if we are in any other position
            # we first hit 0 after that position number of clicks

            # Then we hit 0 every 100 clicks after that
            if current_position == 0:
                clicks_to_zero = 100
            else:
                clicks_to_zero = current_position

            # While we still have enough rotation left to reach position 0 again,
            # count another zero and calculate when we'd hit 0 next
            # (100 clicks later)
            while clicks_to_zero <= rotation_amount:
                zero_count += 1
                clicks_to_zero += 100

            # Actually set the lock position
            current_position = (current_position - rotation_amount) % 100

        elif rotation.startswith("R"):
            rotation_amount = int(rotation.strip("R"))

            # Count how many times we pass through 0 going right

            # Similar logic to above. If we are at zero
            # going right we'll need 100 clicks to get to 0 again

            # Otherwise, we hit 0 after 100 - current position.
            # So at position 25 it'll take 100 - 25
            # (75) steps to get back to 0

            if current_position == 0:
                clicks_to_zero = 100
            else:
                clicks_to_zero = 100 - current_position

            # While we still have enough rotation left to reach position 0 again,
            # count another zero and calculate when we'd hit 0 next
            # (100 clicks later)
            while clicks_to_zero <= rotation_amount:
                zero_count += 1
                clicks_to_zero += 100

            # Actually set the lock position
            current_position = (current_position + rotation_amount) % 100

print(zero_count)