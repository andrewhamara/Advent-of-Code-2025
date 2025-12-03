fname = "input.txt"
with open(fname, 'r') as f:
    instructions = f.readlines()

lock_digits = range(0, 100)
cur_position = 50 # start at 50
num_zeros = 0

for instruction in instructions:
    direction, distance = instruction[0], int(instruction[1:])

    original = cur_position
    remainder = distance % 100
    if direction == 'L':
        remainder = cur_position - remainder
        cur_position = cur_position - distance
    if direction == 'R':
        remainder = cur_position + remainder
        cur_position = cur_position + distance

    zeros = 0

    # case where you go under 0 or over 99
    if original != 0 and (remainder < 0 or remainder > 99):
        zeros += 1
    # case where you end at 0
    elif original != 0 and cur_position % 100 == 0:
        zeros += 1

    # account for repetition in the hundreds
    zeros += abs(distance) // 100
    num_zeros += zeros

    cur_position = lock_digits[cur_position % 100] # handle overflow

print(num_zeros)