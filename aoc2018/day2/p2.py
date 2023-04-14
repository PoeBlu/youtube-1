import Levenshtein

inputs = open('inputs.txt').read().strip().split('\n')

ratios = []

for i1 in inputs:
    ratios.extend(f'{Levenshtein.ratio(i1, i2)}: {i1}/{i2}' for i2 in inputs)
result = sorted([i for i in ratios if not i.startswith('1.0')])[-1]
strings = result.split(': ')[1].split('/')
s1 = strings[0]
s2 = strings[1]

final = ''.join(s1[i] for i in range(len(s1)) if s1[i] == s2[i])
print(final)
