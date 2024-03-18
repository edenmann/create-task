
s1 = 0
s2 = 0
scores = [s1, s2]

result = ["", ""]

rounds = list(range(3))

def player(currentRound):
    if (currentRound%2) == 0:
        return "1"
    else:
        return "2"

def diceRoll():
    return random.randint(1, 6)

def game():
    print("Start")
    for i in rounds:
        print("   - ROUND ", 1, " -")
        print("    SCORES:")
        print("Player 1: ", scores[0], " | Player 2: ", scores[1])
        print("")

        choice = input("Player", player(i), ", do you want to roll? (y or n)")
        if choice == "y":
            while choice == "y":
                roll = diceRoll()
                sc = scores[player(i)-1]
                sc += roll
                print("Rolled:", roll, " Total: ", sc)
                if s1 > 13:
                    result[0] = "Lose"
                elif sc

                choice == input("Roll again? (y or n)")
        else:
