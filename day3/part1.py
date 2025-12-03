fname = 'input.txt'
with open(fname, 'r') as f:
    batches = f.readlines()

total_joltage = 0
for batch in batches:
    num_to_largest_after = {}

    for val in batch.strip():
        for key, value in num_to_largest_after.items():
            num_to_largest_after[key] = max(value, int(val))
        if val not in num_to_largest_after.keys():
            num_to_largest_after[val] = -1

    vals = [int(key + str(val)) for key, val in num_to_largest_after.items() if val != -1]
    joltage = max(vals)
    total_joltage += joltage

print(total_joltage)