fname = 'input.txt'
with open(fname, 'r') as f:
    ranges = f.read().split(',')

total = 0
for val in ranges:
    l, r = map(int, val.split('-'))

    for n in range(l, r+1):
        str_rep = str(n)
        str_rep_len = len(str_rep)
        if str_rep_len % 2 == 0 and str_rep[str_rep_len // 2:] == str_rep[:str_rep_len//2]:
            total += n

print(total)
