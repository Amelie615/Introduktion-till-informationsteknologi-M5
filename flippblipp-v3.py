
def flippblipp(i):
    if i % 3 == 0 and i % 5 == 0:
        return "flipp blipp"
    elif i % 3 == 0:
        return "flipp"
    elif i % 5 == 0:
        return "blipp"
    else: return str(i)

n = 1
print("      ", 1)

activeGame = True

while activeGame == True:
    n = n + 1
    answer = flippblipp(n)
    playerAnswer = input("Nästa: ")
    if answer == playerAnswer:
        continue
    else:
        print("Fel - " + str(answer))
        print()
        print("Game Over")
        
        activeGame = False
        