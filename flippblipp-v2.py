
def flippblipp(i):
    if i % 3 == 0 and i % 5 == 0:
        return "flippblipp"
    elif i % 3 == 0:
        return "flipp"
    elif i % 5 == 0:
        return "blipp"
    else: return str(i)

n = 10

for i in range(1, n+1):
    print(flippblipp(i))