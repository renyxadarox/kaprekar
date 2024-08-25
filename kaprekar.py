import math

max_steps = max_n = 0
try_steps = 100
terminal = set()

d = 4
N = 10 ** d
f = lambda ind, x: x * 10 ** ind
for i in range(N):
    n = i
    m = 0
    print("%0*d" % (d, n), end="")
    step = 0
    while n != 0 and m != n and step < try_steps:
        n = m if step > 0 else n
        lst = [(n // 10 ** j) % 10 for j in range(0, d)]
        lst.sort()
        b = sum([f(ind, x) for ind, x in enumerate(lst)])
        lst.reverse()
        s = sum([f(ind, x) for ind, x in enumerate(lst)])
        m = b - s
        if m == n:
            continue
        if step < 20:
            print(" -> %0*d" % (d, m), end="")
        step += 1
    if step == try_steps:
        print(f" (more than {try_steps} steps)")
    else:
        print(f" ({step} steps)")
    terminal.add(n)
    if max_steps < step:
        max_steps = step
        max_n = i
print("Max steps: %i, first number with %i steps: %0*d" % (max_steps, max_steps, d, max_n))
print("Terminal numbers: %s" % terminal)
