

lock_positions = range(100)
current_position = 50
zero_count = 0

with open('input_day_1.txt', 'r') as puzzle_input:
    for rotation in puzzle_input:
        if rotation.startswith("L"):
            current_position = (current_position - int(rotation.strip("L"))) % 100
        if rotation.startswith("R"):
            current_position = (current_position + int(rotation.strip("R"))) % 100
        if current_position == 0:
            zero_count += 1

print(zero_count)




