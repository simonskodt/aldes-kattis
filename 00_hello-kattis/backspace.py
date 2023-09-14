stack = []

for c in input():
    if c == '<':
        stack.pop()
    else:
        stack.append(c)

final_str = ''.join(stack)
print(final_str)