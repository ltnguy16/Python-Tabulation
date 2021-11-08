#fibonacci using tabulation

def fib_tab(value):
  table = [0] * (value + 2)
  table[1] = 1
  for num in range(value):
    table[num + 1] += table[num]
    table[num + 2] += table[num]
  return table[value]

print(fib_tab(7))
print(fib_tab(8))
print(fib_tab(14))
print(fib_tab(50))