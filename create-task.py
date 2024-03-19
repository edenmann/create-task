import random


scores = [0, 0]
s1 = scores[0]
s2 = scores[1]

result = ["", ""]

rounds = list(range(2))
print(rounds)

def player(currentRound):
    if (currentRound%2) == 0:
        return "1"
    else:
        return "2"

def diceRoll():
    return random.randint(1, 6)

def game():
    print("The objective of this game is to get a higher score than the other player without going above 13")
    print("")

    print(" - GAME START - ")
    for i in rounds:
        print("")
        #print("   - ROUND ", str(i+1), " -")
        print("    SCORES:")
        print("Player 1: ", scores[0], " | Player 2: ", scores[1])
        print("")

        choice = "y"
        print(" - Player", player(i), "turn - ")
        while choice == "y":
            roll = diceRoll()
            scores[int(player(i))-1] += roll
            sc = scores[int(player(i))-1]
            print("Rolled:", roll, " Total: ", sc)

            if sc > 13:
                result[int(player(i))-1] = "Over"
                print("Over")
                choice = "n"
            elif sc == 13:
                result[int(player(i))-1] = "Max"
                print("Max")
                choice = "n"
            elif sc < 13:
                result[int(player(i))-1] = "Under"
                choice = input("Roll again? (y or n)")
                print("")
    
    if 

game()
