fname = 'input.txt'
with open(fname, 'r') as f:
    ranges = f.read().split(',')

total = 0
for val in ranges:
    l, r = map(int, val.split('-'))

    for n in range(l, r+1):
        str_rep = str(n)
        str_rep_len = len(str_rep)

        # only need to consider the first half for patterns
        for i in range(1, 1 + (str_rep_len // 2)):

            # can only be a pattern if it evenly divides the length
            if str_rep_len % i != 0: continue
            pattern = str_rep[:i]

            # hop through the string to check that the pattern matches
            prev = 0
            match = True
            for j in range(i, str_rep_len+i, i):

                # if the pattern ever breaks, break and start with the next pattern length i
                if str_rep[prev:j] != pattern:
                    match = False
                    break
                prev = j

            # if the pattern matches, add the integer n to the total
            if match:
                total += n
                break

print(total)