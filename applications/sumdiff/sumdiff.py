"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
results = {}
sums = {}
differences = {}
q_list = list(q)
for i in q:
    results[i] = f(i)
for elem_one in q_list:
    for elem_two in q_list:
        s = results[elem_one] + results[elem_two]
        d = results[elem_one] - results[elem_two]
        if s in sums:
            sums[s].append((elem_one, elem_two))
        else:
            sums[s] = [(elem_one, elem_two)]
        if d in differences:
            differences[d].append((elem_one, elem_two))
        else:
            differences[d] = [(elem_one, elem_two)]
    s = results[elem_one] * 2

    if t in differences:
        differences[t].append((elem_one, elem_one))
    else:
        differences[t] = [(elem_one, elem_one)]
result = []
for s in sums:
    if s in differences:
        result.append((sums[s], differences[s]))
