fname = "input.txt"
#fname = "smaller.txt"
with open(fname, 'r') as f:
    instructions = f.readlines()

lock_digits = range(0, 100)
cur_position = 50 # start at 50
num_zeros = 0

for instruction in instructions:
    direction, distance = instruction[0], int(instruction[1:])

    if direction == 'L':
        cur_position = cur_position - distance
    if direction == 'R':
        cur_position = cur_position + distance

    cur_position = lock_digits[cur_position % 100] # handle overflow

    if cur_position == 0:
        num_zeros += 1

print(num_zeros)